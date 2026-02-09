"""
AMRIT AI - Permission Manager

Manages explicit consent and permission-gated operations.
Logs all permission requests and grants.
"""

import json
from datetime import datetime, timedelta
from typing import Optional, Dict, List
from enum import Enum
import config
from hidden_storage import HiddenStorageManager


class PermissionType(Enum):
    """Types of permissions that can be requested"""
    DATA_MODIFICATION = "data_modification"
    SYSTEM_UPDATE = "system_update"
    POLICY_CHANGE = "policy_change"
    MODEL_TRAINING = "model_training"
    EXTERNAL_ACCESS = "external_access"
    AUTO_LEARNING = "auto_learning"
    FILE_ACCESS = "file_access"
    NETWORK_ACCESS = "network_access"


class PermissionStatus(Enum):
    """Status of permission requests"""
    PENDING = "pending"
    GRANTED = "granted"
    DENIED = "denied"
    EXPIRED = "expired"
    REVOKED = "revoked"


class PermissionManager:
    """Manages permission system for AMRIT AI"""
    
    def __init__(self, storage_manager: HiddenStorageManager):
        """
        Initialize permission manager
        
        Args:
            storage_manager: Hidden storage manager instance
        """
        self.storage = storage_manager
        self.active_permissions = {}
        self.permission_log = []
        self._load_permissions()
    
    def _load_permissions(self):
        """Load existing permissions from storage"""
        try:
            stored_data = self.storage.retrieve_data(
                'behavior_profiles', 
                'active_permissions'
            )
            if stored_data:
                self.active_permissions = stored_data
            
            stored_log = self.storage.retrieve_data(
                'learning_logs',
                'permission_log'
            )
            if stored_log:
                self.permission_log = stored_log
        except:
            pass
    
    def _save_permissions(self):
        """Save permissions to encrypted storage"""
        self.storage.store_data(
            'behavior_profiles',
            'active_permissions',
            self.active_permissions
        )
        self.storage.store_data(
            'learning_logs',
            'permission_log',
            self.permission_log
        )
    
    def request_permission(self, permission_type: PermissionType, 
                          reason: str, metadata: Optional[Dict] = None) -> str:
        """
        Request permission for an operation
        
        Args:
            permission_type: Type of permission needed
            reason: Human-readable reason for permission
            metadata: Additional context information
            
        Returns:
            Permission request ID
        """
        request_id = f"perm_{datetime.now().timestamp()}_{permission_type.value}"
        
        permission_request = {
            'request_id': request_id,
            'type': permission_type.value,
            'reason': reason,
            'metadata': metadata or {},
            'requested_at': datetime.now().isoformat(),
            'status': PermissionStatus.PENDING.value,
            'expires_at': None,
            'granted_at': None,
            'denied_at': None,
        }
        
        self.active_permissions[request_id] = permission_request
        self.permission_log.append(permission_request.copy())
        self._save_permissions()
        
        return request_id
    
    def grant_permission(self, request_id: str, 
                        duration: Optional[int] = None) -> bool:
        """
        Grant a permission request
        
        Args:
            request_id: Permission request ID
            duration: Optional duration in seconds (default from config)
            
        Returns:
            True if granted successfully
        """
        if request_id not in self.active_permissions:
            return False
        
        permission = self.active_permissions[request_id]
        
        if permission['status'] != PermissionStatus.PENDING.value:
            return False
        
        # Calculate expiry time
        duration = duration or config.PERMISSION_EXPIRY_TIME
        expiry_time = datetime.now() + timedelta(seconds=duration)
        
        permission['status'] = PermissionStatus.GRANTED.value
        permission['granted_at'] = datetime.now().isoformat()
        permission['expires_at'] = expiry_time.isoformat()
        
        # Update log
        log_entry = permission.copy()
        log_entry['action'] = 'granted'
        self.permission_log.append(log_entry)
        
        self._save_permissions()
        return True
    
    def deny_permission(self, request_id: str, reason: str = "") -> bool:
        """
        Deny a permission request
        
        Args:
            request_id: Permission request ID
            reason: Reason for denial
            
        Returns:
            True if denied successfully
        """
        if request_id not in self.active_permissions:
            return False
        
        permission = self.active_permissions[request_id]
        
        if permission['status'] != PermissionStatus.PENDING.value:
            return False
        
        permission['status'] = PermissionStatus.DENIED.value
        permission['denied_at'] = datetime.now().isoformat()
        permission['denial_reason'] = reason
        
        # Update log
        log_entry = permission.copy()
        log_entry['action'] = 'denied'
        self.permission_log.append(log_entry)
        
        self._save_permissions()
        return True
    
    def check_permission(self, permission_type: PermissionType) -> bool:
        """
        Check if there's an active permission for an operation type
        
        Args:
            permission_type: Type of permission to check
            
        Returns:
            True if permission is active and valid
        """
        current_time = datetime.now()
        
        for request_id, permission in self.active_permissions.items():
            if permission['type'] != permission_type.value:
                continue
            
            if permission['status'] != PermissionStatus.GRANTED.value:
                continue
            
            # Check expiry
            if permission['expires_at']:
                expiry_time = datetime.fromisoformat(permission['expires_at'])
                if current_time > expiry_time:
                    # Mark as expired
                    permission['status'] = PermissionStatus.EXPIRED.value
                    self._save_permissions()
                    continue
            
            return True
        
        return False
    
    def revoke_permission(self, request_id: str) -> bool:
        """
        Revoke an active permission
        
        Args:
            request_id: Permission request ID
            
        Returns:
            True if revoked successfully
        """
        if request_id not in self.active_permissions:
            return False
        
        permission = self.active_permissions[request_id]
        permission['status'] = PermissionStatus.REVOKED.value
        permission['revoked_at'] = datetime.now().isoformat()
        
        # Update log
        log_entry = permission.copy()
        log_entry['action'] = 'revoked'
        self.permission_log.append(log_entry)
        
        self._save_permissions()
        return True
    
    def revoke_all_permissions(self, permission_type: Optional[PermissionType] = None):
        """
        Revoke all active permissions, optionally filtered by type
        
        Args:
            permission_type: Optional filter by permission type
        """
        for request_id, permission in self.active_permissions.items():
            if permission['status'] != PermissionStatus.GRANTED.value:
                continue
            
            if permission_type and permission['type'] != permission_type.value:
                continue
            
            self.revoke_permission(request_id)
    
    def get_permission_history(self, limit: int = 100) -> List[Dict]:
        """
        Get permission history log
        
        Args:
            limit: Maximum number of entries to return
            
        Returns:
            List of permission log entries
        """
        return self.permission_log[-limit:]
    
    def get_active_permissions(self) -> List[Dict]:
        """
        Get all currently active permissions
        
        Returns:
            List of active permission objects
        """
        active = []
        current_time = datetime.now()
        
        for request_id, permission in self.active_permissions.items():
            if permission['status'] != PermissionStatus.GRANTED.value:
                continue
            
            # Check expiry
            if permission['expires_at']:
                expiry_time = datetime.fromisoformat(permission['expires_at'])
                if current_time > expiry_time:
                    continue
            
            active.append(permission)
        
        return active
    
    def cleanup_expired_permissions(self):
        """Remove expired permissions from active list"""
        current_time = datetime.now()
        to_remove = []
        
        for request_id, permission in self.active_permissions.items():
            if permission['status'] not in [
                PermissionStatus.GRANTED.value,
                PermissionStatus.PENDING.value
            ]:
                to_remove.append(request_id)
                continue
            
            if permission['expires_at']:
                expiry_time = datetime.fromisoformat(permission['expires_at'])
                if current_time > expiry_time:
                    permission['status'] = PermissionStatus.EXPIRED.value
        
        for request_id in to_remove:
            del self.active_permissions[request_id]
        
        if to_remove:
            self._save_permissions()
    
    def require_permission(self, permission_type: PermissionType, 
                          reason: str, auto_request: bool = True) -> bool:
        """
        Require permission for an operation, with option to auto-request
        
        Args:
            permission_type: Type of permission needed
            reason: Reason for permission
            auto_request: Whether to automatically create request if not exists
            
        Returns:
            True if permission is available
        """
        # Check if permission already exists
        if self.check_permission(permission_type):
            return True
        
        # Auto-request if enabled
        if auto_request:
            request_id = self.request_permission(
                permission_type,
                reason,
                {'auto_requested': True}
            )
            # Note: This still requires manual granting
            # The request is logged for user review
        
        return False
    
    def get_statistics(self) -> Dict:
        """
        Get permission statistics
        
        Returns:
            Dictionary with statistics
        """
        stats = {
            'total_requests': len(self.permission_log),
            'active_permissions': len(self.get_active_permissions()),
            'by_type': {},
            'by_status': {}
        }
        
        for entry in self.permission_log:
            ptype = entry.get('type', 'unknown')
            status = entry.get('status', 'unknown')
            
            stats['by_type'][ptype] = stats['by_type'].get(ptype, 0) + 1
            stats['by_status'][status] = stats['by_status'].get(status, 0) + 1
        
        return stats
