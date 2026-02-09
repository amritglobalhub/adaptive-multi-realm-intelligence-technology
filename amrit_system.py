"""
AMRIT AI - Main System

Core orchestration for Adaptive Multi-Realm Intelligence Technology.
"""

import sys
from typing import Optional, Dict, Any
from datetime import datetime
import numpy as np
import config
from hidden_storage import HiddenStorageManager
from permission_manager import PermissionManager, PermissionType
from owner_recognition import OwnerRecognitionEngine
from self_learning import SelfLearningEngine
from data_mining import DataMiningPipeline
from ui_personalization import UIPersonalizationEngine


class AMRITSystem:
    """Main AMRIT AI system orchestrator"""
    
    def __init__(self, master_password: str):
        """
        Initialize AMRIT AI system
        
        Args:
            master_password: Master password for encryption
        """
        self.master_password = master_password
        self.initialized = False
        self.session_active = False
        self.session_start_time = None
        
        # Initialize subsystems
        self._initialize_subsystems()
    
    def _initialize_subsystems(self):
        """Initialize all AMRIT subsystems"""
        print("🔮 Initializing AMRIT AI System...")
        
        try:
            # Storage layer
            print("  📦 Initializing hidden storage...")
            self.storage = HiddenStorageManager(self.master_password)
            self.storage.initialize()
            
            # Permission system
            print("  🔐 Initializing permission manager...")
            self.permissions = PermissionManager(self.storage)
            
            # Owner recognition
            print("  👤 Initializing owner recognition...")
            self.owner_recognition = OwnerRecognitionEngine(self.storage)
            
            # Self-learning engine
            print("  🧠 Initializing self-learning engine...")
            self.learning_engine = SelfLearningEngine(self.storage, self.permissions)
            
            # Data mining
            print("  ⛏️  Initializing data mining pipeline...")
            self.data_mining = DataMiningPipeline(self.storage)
            
            # UI personalization
            print("  🎨 Initializing UI personalization...")
            self.ui_engine = UIPersonalizationEngine(self.storage)
            
            self.initialized = True
            print("✅ AMRIT AI System initialized successfully!")
            
        except Exception as e:
            print(f"❌ Error initializing AMRIT: {e}")
            self.initialized = False
    
    def authenticate_owner(self, audio_data: Optional[np.ndarray] = None,
                          text: Optional[str] = None,
                          behavioral_data: Optional[Dict] = None) -> bool:
        """
        Authenticate the owner using multi-modal biometrics
        
        Args:
            audio_data: Optional voice sample
            text: Optional text sample
            behavioral_data: Optional behavioral data
            
        Returns:
            True if authenticated successfully
        """
        if not self.initialized:
            print("❌ System not initialized")
            return False
        
        print("🔍 Authenticating owner...")
        
        is_owner, confidence = self.owner_recognition.verify_owner(
            audio_data, text, behavioral_data
        )
        
        if is_owner:
            print(f"✅ Owner authenticated (confidence: {confidence:.2%})")
            self.session_active = True
            self.session_start_time = datetime.now()
            
            # Update profile if confidence is high
            if confidence > 0.9:
                self.owner_recognition.update_profile(audio_data, text, behavioral_data)
            
            return True
        else:
            print(f"❌ Authentication failed (confidence: {confidence:.2%})")
            return False
    
    def enroll_owner(self, audio_samples: list, text_samples: list,
                    behavioral_samples: list) -> bool:
        """
        Enroll owner for first-time setup
        
        Args:
            audio_samples: List of voice samples
            text_samples: List of text samples
            behavioral_samples: List of behavioral data
            
        Returns:
            True if enrollment successful
        """
        print("📝 Enrolling owner biometrics...")
        
        success = self.owner_recognition.enroll_owner(
            audio_samples, text_samples, behavioral_samples
        )
        
        if success:
            print("✅ Owner enrolled successfully!")
            
            # Grant initial learning permission
            request_id = self.permissions.request_permission(
                PermissionType.AUTO_LEARNING,
                "Initial auto-learning setup",
                {'initial_setup': True}
            )
            self.permissions.grant_permission(request_id, duration=86400)  # 24 hours
            
            return True
        else:
            print("❌ Owner enrollment failed")
            return False
    
    def record_interaction(self, interaction_type: str, data: Dict) -> str:
        """
        Record an interaction for learning
        
        Args:
            interaction_type: Type of interaction
            data: Interaction data
            
        Returns:
            Interaction ID
        """
        if not self.session_active:
            print("⚠️  No active session")
            return ""
        
        interaction_id = self.learning_engine.record_interaction(
            interaction_type, data
        )
        
        return interaction_id
    
    def request_permission(self, permission_type: PermissionType, 
                          reason: str) -> str:
        """
        Request permission for an operation
        
        Args:
            permission_type: Type of permission
            reason: Reason for request
            
        Returns:
            Permission request ID
        """
        print(f"🔔 Permission requested: {permission_type.value}")
        print(f"   Reason: {reason}")
        
        request_id = self.permissions.request_permission(
            permission_type, reason
        )
        
        print(f"   Request ID: {request_id}")
        print("   Awaiting approval...")
        
        return request_id
    
    def grant_permission(self, request_id: str, duration: Optional[int] = None) -> bool:
        """
        Grant a permission request
        
        Args:
            request_id: Permission request ID
            duration: Optional duration in seconds
            
        Returns:
            True if granted successfully
        """
        success = self.permissions.grant_permission(request_id, duration)
        
        if success:
            print(f"✅ Permission granted: {request_id}")
        else:
            print(f"❌ Failed to grant permission: {request_id}")
        
        return success
    
    def get_learned_patterns(self) -> Dict:
        """Get all learned patterns"""
        return self.learning_engine.get_learned_patterns()
    
    def get_preferences(self) -> Dict:
        """Get learned preferences"""
        return self.learning_engine.get_preferences()
    
    def get_personalization_profile(self) -> Dict:
        """Get personalization profile"""
        return self.data_mining.get_personalization_profile()
    
    def run_data_analysis(self) -> Dict:
        """
        Run complete data mining analysis
        
        Returns:
            Analysis insights
        """
        if not self.permissions.check_permission(PermissionType.DATA_MODIFICATION):
            print("⚠️  Data analysis requires permission")
            return {}
        
        print("🔬 Running data analysis...")
        
        insights = self.data_mining.run_full_analysis(
            self.learning_engine.interaction_history,
            self.learning_engine.linguistic_patterns
        )
        
        print(f"✅ Analysis complete! Found {insights.get('sample_size', 0)} interactions")
        
        return insights
    
    def generate_personalized_ui(self) -> Dict:
        """
        Generate personalized UI based on learned preferences
        
        Returns:
            UI configuration
        """
        if not self.permissions.check_permission(PermissionType.SYSTEM_UPDATE):
            print("⚠️  UI generation requires permission")
            return {}
        
        print("🎨 Generating personalized UI...")
        
        # Get personalization profile
        profile = self.data_mining.get_personalization_profile()
        patterns = self.learning_engine.get_learned_patterns()
        
        # Generate UI
        ui_config = self.ui_engine.create_personalized_ui(profile, patterns)
        
        print("✅ Personalized UI generated!")
        
        return ui_config
    
    def get_system_status(self) -> Dict:
        """
        Get comprehensive system status
        
        Returns:
            Status dictionary
        """
        status = {
            'system_name': config.SYSTEM_NAME,
            'version': config.SYSTEM_VERSION,
            'initialized': self.initialized,
            'session_active': self.session_active,
            'owner_enrolled': self.owner_recognition.owner_profile is not None,
            'learning_enabled': config.ENABLE_AUTO_LEARNING,
            'permissions': {
                'active': len(self.permissions.get_active_permissions()),
                'statistics': self.permissions.get_statistics()
            },
            'learning': self.learning_engine.get_interaction_statistics(),
            'owner_profile': self.owner_recognition.get_profile_stats(),
            'timestamp': datetime.now().isoformat()
        }
        
        return status
    
    def print_status(self):
        """Print system status in readable format"""
        status = self.get_system_status()
        
        print("\n" + "="*60)
        print(f"🔮 {status['system_name']} v{status['version']}")
        print("="*60)
        print(f"Status: {'🟢 Active' if status['session_active'] else '⚪ Inactive'}")
        print(f"Owner Enrolled: {'✅ Yes' if status['owner_enrolled'] else '❌ No'}")
        print(f"Auto-Learning: {'✅ Enabled' if status['learning_enabled'] else '❌ Disabled'}")
        print(f"\n📊 Statistics:")
        print(f"  • Total Interactions: {status['learning']['total_interactions']}")
        print(f"  • Learned Interactions: {status['learning']['learned_interactions']}")
        print(f"  • Active Permissions: {status['permissions']['active']}")
        print(f"  • Patterns Learned: {status['learning']['patterns_learned']}")
        print("="*60 + "\n")
    
    def end_session(self):
        """End current session and cleanup"""
        if self.session_active:
            print("👋 Ending session...")
            
            # Save all state
            self.learning_engine._save_learning_state()
            self.permissions._save_permissions()
            
            # Clear cache if configured
            if config.CLEAR_CACHE_ON_EXIT:
                self.storage.clear_cache()
            
            self.session_active = False
            print("✅ Session ended")
    
    def secure_wipe(self) -> bool:
        """
        Securely wipe all data (WARNING: IRREVERSIBLE)
        
        Returns:
            True if wiped successfully
        """
        print("⚠️  WARNING: This will delete all AMRIT data permanently!")
        confirmation = input("Type 'WIPE' to confirm: ")
        
        if confirmation == "WIPE":
            print("🗑️  Wiping all data...")
            success = self.storage.secure_wipe()
            
            if success:
                print("✅ All data wiped securely")
            else:
                print("❌ Failed to wipe data")
            
            return success
        else:
            print("❌ Wipe cancelled")
            return False


def main():
    """Main entry point for AMRIT AI"""
    print("\n" + "="*60)
    print("🔮 AMRIT AI - Adaptive Multi-Realm Intelligence Technology")
    print("="*60 + "\n")
    
    # Initialize system
    master_password = input("Enter master password: ")
    
    if not master_password:
        print("❌ Master password required")
        return
    
    system = AMRITSystem(master_password)
    
    if not system.initialized:
        print("❌ Failed to initialize system")
        return
    
    # Check if owner is enrolled
    if not system.owner_recognition.owner_profile:
        print("\n📝 First-time setup: Owner enrollment required")
        print("   Please provide at least 3 samples for enrollment")
        print("   (For demo, using placeholder samples)")
        
        # Demo: Create placeholder samples
        audio_samples = [np.random.randn(16000) for _ in range(3)]
        text_samples = ["Hello AMRIT", "This is my voice", "Initialize system"]
        behavioral_samples = [
            {'timestamp': datetime.now().isoformat(), 'duration': 10},
            {'timestamp': datetime.now().isoformat(), 'duration': 15},
            {'timestamp': datetime.now().isoformat(), 'duration': 12}
        ]
        
        system.enroll_owner(audio_samples, text_samples, behavioral_samples)
    
    # Authenticate
    print("\n🔐 Authenticating...")
    # Demo: Use placeholder for authentication
    audio = np.random.randn(16000)
    authenticated = system.authenticate_owner(audio_data=audio, text="Hello AMRIT")
    
    if not authenticated:
        print("❌ Authentication failed")
        return
    
    # Show status
    system.print_status()
    
    # Demo: Record some interactions
    print("📝 Recording sample interactions...")
    system.record_interaction('command', {
        'command': 'start_learning',
        'context': {'mode': 'active'},
        'success': True
    })
    
    system.record_interaction('query', {
        'query': 'what is machine learning',
        'response': 'Machine learning is a field of AI...',
        'satisfaction': 0.9
    })
    
    system.record_interaction('conversation', {
        'text': 'I prefer detailed responses with examples',
    })
    
    print("✅ Sample interactions recorded")
    
    # Show final status
    system.print_status()
    
    # End session
    system.end_session()
    
    print("\n✅ AMRIT AI demo completed successfully!\n")


if __name__ == "__main__":
    main()
