"""
Permission Management System
Handles voice-based permission requests and management
"""

import json
from datetime import datetime
from typing import Dict, List, Optional, Any


class Permission:
    """Represents a single permission"""
    
    def __init__(self, permission_id: str, name: str, description: str):
        self.permission_id = permission_id
        self.name = name
        self.description = description
        self.granted = False
        self.granted_at = None
        self.granted_by_voice = False
        
    def grant(self, by_voice: bool = True):
        """Grant permission"""
        self.granted = True
        self.granted_at = datetime.now().isoformat()
        self.granted_by_voice = by_voice
        
    def revoke(self):
        """Revoke permission"""
        self.granted = False
        self.granted_at = None
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "permission_id": self.permission_id,
            "name": self.name,
            "description": self.description,
            "granted": self.granted,
            "granted_at": self.granted_at,
            "granted_by_voice": self.granted_by_voice
        }


class PermissionManager:
    """
    Permission management system with voice-based confirmation
    
    AMRIT: "क्या मैं कोड generate कर सकता हूँ?"
    You: "हाँ, करो"
    
    हर बार voice में permission लेगा
    """
    
    def __init__(self):
        self.permissions = {}
        self.permission_history = []
        self.initialize_permissions()
        
    def initialize_permissions(self):
        """Initialize default permissions"""
        default_permissions = [
            ("code_generation", "Code Generation", "Generate code automatically"),
            ("learning_preferences", "Learning Preferences", "Learn from user preferences"),
            ("offline_mode", "Offline Mode", "Work without internet connection"),
            ("auto_save", "Auto Save", "Automatically save projects"),
            ("file_access", "File Access", "Access and modify files"),
            ("data_sync", "Data Sync", "Sync data across devices"),
            ("voice_recording", "Voice Recording", "Record voice inputs"),
            ("analytics", "Analytics", "Collect usage analytics"),
            ("notifications", "Notifications", "Send notifications"),
            ("camera_access", "Camera Access", "Access device camera"),
            ("microphone_access", "Microphone Access", "Access device microphone"),
            ("location_access", "Location Access", "Access device location")
        ]
        
        for perm_id, name, description in default_permissions:
            self.permissions[perm_id] = Permission(perm_id, name, description)
    
    def request_permission(self, permission_id: str) -> Dict[str, Any]:
        """
        Request permission with voice prompt
        
        Returns the question to ask user
        """
        
        if permission_id not in self.permissions:
            return {
                "status": "error",
                "message": f"Permission {permission_id} not found"
            }
        
        permission = self.permissions[permission_id]
        
        # Generate Hindi-English voice prompt
        prompts = {
            "code_generation": "क्या मैं कोड generate कर सकता हूँ?",
            "learning_preferences": "क्या मैं तुम्हारे preferences सीख सकता हूँ?",
            "offline_mode": "क्या मैं offline काम कर सकता हूँ?",
            "auto_save": "क्या मैं projects auto-save कर सकता हूँ?",
            "file_access": "क्या मैं files access कर सकता हूँ?",
            "data_sync": "क्या मैं data sync कर सकता हूँ?",
            "voice_recording": "क्या मैं voice record कर सकता हूँ?",
            "analytics": "क्या मैं analytics collect कर सकता हूँ?",
            "notifications": "क्या मैं notifications भेज सकता हूँ?",
            "camera_access": "क्या मैं camera access कर सकता हूँ?",
            "microphone_access": "क्या मैं microphone access कर सकता हूँ?",
            "location_access": "क्या मैं location access कर सकता हूँ?"
        }
        
        prompt = prompts.get(permission_id, f"क्या मैं {permission.name} use कर सकता हूँ?")
        
        return {
            "status": "requesting",
            "permission_id": permission_id,
            "permission_name": permission.name,
            "voice_prompt": prompt,
            "awaiting_response": True,
            "timestamp": datetime.now().isoformat()
        }
    
    def process_voice_response(self, permission_id: str, voice_response: str) -> Dict[str, Any]:
        """
        Process user's voice response to permission request
        
        Accepts:
        - "हाँ" / "Yes" / "करो" / "ठीक है" → Grant
        - "नहीं" / "No" / "मत करो" → Deny
        - "पूरी तरह" / "सब कुछ" → Grant with full access
        """
        
        if permission_id not in self.permissions:
            return {
                "status": "error",
                "message": f"Permission {permission_id} not found"
            }
        
        permission = self.permissions[permission_id]
        response_lower = voice_response.lower()
        
        # Check for positive responses
        positive_keywords = ["हाँ", "yes", "करो", "ठीक है", "okay", "sure", "पूरी तरह", "सब कुछ"]
        is_granted = any(keyword in response_lower for keyword in positive_keywords)
        
        result = {
            "permission_id": permission_id,
            "permission_name": permission.name,
            "voice_response": voice_response,
            "timestamp": datetime.now().isoformat()
        }
        
        if is_granted:
            permission.grant(by_voice=True)
            result["status"] = "granted"
            result["message"] = f"✓ {permission.name} activated"
            
            # Special handling for certain permissions
            if "पूरी तरह" in response_lower or "सब कुछ" in response_lower:
                result["access_level"] = "full"
            else:
                result["access_level"] = "standard"
        else:
            result["status"] = "denied"
            result["message"] = f"✗ {permission.name} not activated"
        
        # Record in history
        self.permission_history.append({
            "permission_id": permission_id,
            "action": "granted" if is_granted else "denied",
            "voice_response": voice_response,
            "timestamp": result["timestamp"]
        })
        
        return result
    
    def request_multiple_permissions(self, permission_ids: List[str]) -> List[Dict[str, Any]]:
        """Request multiple permissions sequentially"""
        requests = []
        for perm_id in permission_ids:
            requests.append(self.request_permission(perm_id))
        return requests
    
    def get_permission_status(self, permission_id: str) -> Dict[str, Any]:
        """Get status of a specific permission"""
        if permission_id not in self.permissions:
            return {"status": "not_found"}
        
        return self.permissions[permission_id].to_dict()
    
    def get_all_permissions(self) -> Dict[str, Dict[str, Any]]:
        """Get all permissions and their status"""
        return {
            perm_id: perm.to_dict()
            for perm_id, perm in self.permissions.items()
        }
    
    def check_permission(self, permission_id: str) -> bool:
        """Check if permission is granted"""
        if permission_id not in self.permissions:
            return False
        return self.permissions[permission_id].granted


class VoiceConfirmation:
    """
    Voice confirmation system for major operations
    
    AMRIT: "मैं तुम्हारे लिए यह code generate करूँ?"
    You: "हाँ" या "नहीं" या "इसमें यह बदलाव कर"
    """
    
    def __init__(self):
        self.pending_confirmations = {}
        self.confirmation_history = []
        
    def request_confirmation(self, operation: str, details: str) -> Dict[str, Any]:
        """Request confirmation for an operation"""
        
        confirmation_id = f"conf_{int(datetime.now().timestamp())}"
        
        # Generate voice prompts for different operations
        prompts = {
            "code_generation": f"मैं तुम्हारे लिए यह code generate करूँ? ({details})",
            "design_creation": f"क्या मैं यह design use करूँ? ({details})",
            "file_modification": f"क्या मैं यह file modify करूँ? ({details})",
            "data_deletion": f"क्या मैं यह data delete करूँ? ({details})",
            "project_creation": f"क्या मैं नया project create करूँ? ({details})"
        }
        
        prompt = prompts.get(operation, f"क्या मैं यह operation करूँ? ({details})")
        
        confirmation = {
            "confirmation_id": confirmation_id,
            "operation": operation,
            "details": details,
            "voice_prompt": prompt,
            "status": "pending",
            "timestamp": datetime.now().isoformat()
        }
        
        self.pending_confirmations[confirmation_id] = confirmation
        return confirmation
    
    def process_confirmation_response(self, confirmation_id: str, voice_response: str) -> Dict[str, Any]:
        """Process user's confirmation response"""
        
        if confirmation_id not in self.pending_confirmations:
            return {
                "status": "error",
                "message": "Confirmation not found"
            }
        
        confirmation = self.pending_confirmations[confirmation_id]
        response_lower = voice_response.lower()
        
        # Check response
        positive_keywords = ["हाँ", "yes", "करो", "ठीक है", "okay", "sure", "बहुत अच्छा"]
        negative_keywords = ["नहीं", "no", "मत करो", "not"]
        modification_keywords = ["बदलाव", "change", "modify", "edit"]
        
        result = {
            "confirmation_id": confirmation_id,
            "operation": confirmation["operation"],
            "voice_response": voice_response,
            "timestamp": datetime.now().isoformat()
        }
        
        if any(keyword in response_lower for keyword in positive_keywords):
            result["status"] = "confirmed"
            result["action"] = "proceed"
            result["message"] = "✓ Operation confirmed"
            confirmation["status"] = "confirmed"
        elif any(keyword in response_lower for keyword in negative_keywords):
            result["status"] = "rejected"
            result["action"] = "cancel"
            result["message"] = "✗ Operation cancelled"
            confirmation["status"] = "rejected"
        elif any(keyword in response_lower for keyword in modification_keywords):
            result["status"] = "modification_requested"
            result["action"] = "modify"
            result["message"] = "⚠ Modification requested"
            result["modification_details"] = voice_response
            confirmation["status"] = "modification_requested"
        else:
            result["status"] = "unclear"
            result["action"] = "repeat_prompt"
            result["message"] = "कृपया फिर से बताएं - हाँ या नहीं?"
        
        # Record in history
        self.confirmation_history.append(result)
        
        return result


if __name__ == "__main__":
    print("=== AMRIT AI Permission Management Test ===\n")
    
    # Initialize permission manager
    perm_manager = PermissionManager()
    
    # Request permissions
    print("--- Permission Requests ---")
    
    # Request code generation permission
    request = perm_manager.request_permission("code_generation")
    print(f"AMRIT: {request['voice_prompt']}")
    
    # User responds
    response = perm_manager.process_voice_response("code_generation", "हाँ, करो")
    print(f"You: हाँ, करो")
    print(f"Result: {response['message']}\n")
    
    # Request learning permission
    request = perm_manager.request_permission("learning_preferences")
    print(f"AMRIT: {request['voice_prompt']}")
    
    response = perm_manager.process_voice_response("learning_preferences", "पूरी तरह, सब कुछ सीख")
    print(f"You: पूरी तरह, सब कुछ सीख")
    print(f"Result: {response['message']}")
    print(f"Access Level: {response['access_level']}\n")
    
    # Request offline mode
    request = perm_manager.request_permission("offline_mode")
    print(f"AMRIT: {request['voice_prompt']}")
    
    response = perm_manager.process_voice_response("offline_mode", "हाँ, बिना internet के भी करो")
    print(f"You: हाँ, बिना internet के भी करो")
    print(f"Result: {response['message']}\n")
    
    # Voice confirmation system
    print("--- Voice Confirmation System ---")
    voice_conf = VoiceConfirmation()
    
    # Request confirmation for code generation
    conf_request = voice_conf.request_confirmation(
        "code_generation",
        "E-commerce app with payment integration"
    )
    print(f"AMRIT: {conf_request['voice_prompt']}")
    
    # User confirms
    conf_response = voice_conf.process_confirmation_response(
        conf_request['confirmation_id'],
        "हाँ, बहुत अच्छा है"
    )
    print(f"You: हाँ, बहुत अच्छा है")
    print(f"Result: {conf_response['message']}\n")
    
    # Check permission status
    print("--- Permission Status ---")
    all_perms = perm_manager.get_all_permissions()
    granted_count = sum(1 for p in all_perms.values() if p['granted'])
    print(f"✓ Total permissions: {len(all_perms)}")
    print(f"✓ Granted permissions: {granted_count}")
    print(f"✓ Code generation: {perm_manager.check_permission('code_generation')}")
    print(f"✓ Offline mode: {perm_manager.check_permission('offline_mode')}")
    
    print("\n✓ Permission Management System Ready!")
