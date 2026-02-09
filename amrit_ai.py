"""
AMRIT AI - Main Controller
Complete Autonomous System integrating all components
"""

import sys
from typing import Dict, List, Optional, Any
from datetime import datetime

import amrit_config as config
from voice_learning import voice_learning_system
from code_generator import code_generator
from design_generator import design_generator
from learning_system import learning_system
from secure_storage import secure_storage


class AmritAI:
    """
    Main AMRIT AI Controller
    Integrates all subsystems: voice learning, code generation, design generation,
    learning/adaptation, and secure storage
    """
    
    def __init__(self):
        self.version = config.SYSTEM_VERSION
        self.name = config.SYSTEM_NAME
        self.user_name = config.USER_NAME
        self.initialized = False
        self.activity_log = []
        
        print(f"🔮 Initializing {self.name} v{self.version}...")
        self._initialize_system()
    
    def _initialize_system(self):
        """Initialize AMRIT AI system"""
        
        # Verify all subsystems
        subsystems = {
            'Voice Learning': voice_learning_system,
            'Code Generator': code_generator,
            'Design Generator': design_generator,
            'Learning System': learning_system,
            'Secure Storage': secure_storage
        }
        
        print("\n📦 Checking subsystems...")
        for name, system in subsystems.items():
            status = "✓" if system else "✗"
            print(f"  {status} {name}")
        
        # Check vault status
        vault_status = secure_storage.get_vault_status()
        print(f"\n🔐 Secure Vault: {'Initialized' if vault_status['initialized'] else 'Not Initialized'}")
        print(f"  Encryption: {vault_status['security_level']}")
        print(f"  Voice Biometrics: {vault_status['voice_biometrics_count']}")
        print(f"  Projects: {vault_status['projects_count']}")
        print(f"  Designs: {vault_status['designs_count']}")
        
        # Get voice learning status
        voice_stats = voice_learning_system.get_voice_statistics()
        print(f"\n🎤 Voice Learning System:")
        print(f"  Phase: {voice_stats['current_phase']}")
        print(f"  Samples: {voice_stats['samples_collected']}")
        print(f"  Progress: {voice_stats['progress_percentage']:.1f}%")
        
        # Get learning progress
        learning_progress = learning_system.get_learning_progress()
        print(f"\n🧠 Learning System:")
        print(f"  Phase: {learning_progress['current_phase']}")
        print(f"  Progress: {learning_progress['progress_percentage']:.1f}%")
        print(f"  Interactions: {learning_progress['statistics']['total_interactions']}")
        
        self.initialized = True
        print(f"\n✅ {self.name} initialized successfully!")
        print(f"👤 User: {self.user_name}")
    
    def process_voice_command(self, command: str, audio_data: Optional[bytes] = None) -> Dict[str, Any]:
        """
        Process voice command from user
        
        Args:
            command: Text transcription of voice command
            audio_data: Optional raw audio data for voice learning
        
        Returns:
            Response with command execution result
        """
        print(f"\n🎤 Processing command: '{command}'")
        
        # Record voice sample for learning (if audio provided)
        if audio_data:
            voice_result = voice_learning_system.record_voice_sample(audio_data, command)
            print(f"  Voice Learning: {voice_result['message']}")
        
        # Record interaction for learning
        learning_system.record_interaction('voice_command', {'command': command})
        
        # Log activity
        self._log_activity('voice_command', command)
        
        # Parse and execute command
        result = self._execute_command(command)
        
        # Learn from execution
        voice_learning_system.learn_preference_from_voice(command)
        
        return result
    
    def _execute_command(self, command: str) -> Dict[str, Any]:
        """Execute parsed command"""
        
        command_lower = command.lower()
        
        # Code generation commands
        if any(keyword in command_lower for keyword in ['code', 'website', 'app', 'api', 'program', 'बना']):
            return self._handle_code_generation(command)
        
        # Design generation commands
        elif any(keyword in command_lower for keyword in ['design', 'logo', 'ui', 'ux', 'brand']):
            return self._handle_design_generation(command)
        
        # Status/Info commands
        elif any(keyword in command_lower for keyword in ['status', 'progress', 'stats', 'info']):
            return self._handle_status_request(command)
        
        # Suggestion commands
        elif any(keyword in command_lower for keyword in ['suggest', 'recommend', 'advice']):
            return self._handle_suggestion_request(command)
        
        # Help command
        elif 'help' in command_lower:
            return self._handle_help_request()
        
        else:
            return {
                'success': False,
                'message': 'Command not recognized. Say "help" for available commands.',
                'suggestions': learning_system.make_suggestion(command)['suggestions']
            }
    
    def _handle_code_generation(self, command: str) -> Dict[str, Any]:
        """Handle code generation request"""
        
        # Parse command to extract details
        language = self._extract_language(command)
        project_type = self._extract_project_type(command)
        
        print(f"  Generating {language} code for {project_type}...")
        
        result = code_generator.generate_code(
            description=command,
            language=language,
            project_type=project_type
        )
        
        if result['success']:
            print(f"  ✅ Code generated successfully!")
            print(f"  Project ID: {result['project_id']}")
            self._log_activity('code_generated', result['project_id'])
        
        return result
    
    def _handle_design_generation(self, command: str) -> Dict[str, Any]:
        """Handle design generation request"""
        
        # Parse command to extract design type
        design_type = self._extract_design_type(command)
        
        print(f"  Generating {design_type}...")
        
        result = design_generator.generate_design(
            design_type=design_type,
            description=command
        )
        
        if result['success']:
            print(f"  ✅ Design generated successfully!")
            print(f"  Design ID: {result['design_id']}")
            self._log_activity('design_generated', result['design_id'])
        
        return result
    
    def _handle_status_request(self, command: str) -> Dict[str, Any]:
        """Handle status/progress request"""
        
        voice_stats = voice_learning_system.get_voice_statistics()
        learning_progress = learning_system.get_learning_progress()
        vault_status = secure_storage.get_vault_status()
        
        status = {
            'success': True,
            'system_name': self.name,
            'version': self.version,
            'user': self.user_name,
            'voice_learning': voice_stats,
            'learning_progress': learning_progress,
            'vault_status': vault_status,
            'activity_count': len(self.activity_log)
        }
        
        print("\n📊 System Status:")
        print(f"  Voice Phase: {voice_stats['current_phase']} ({voice_stats['progress_percentage']:.1f}%)")
        print(f"  Learning Phase: {learning_progress['current_phase']} ({learning_progress['progress_percentage']:.1f}%)")
        print(f"  Projects: {vault_status['projects_count']}")
        print(f"  Designs: {vault_status['designs_count']}")
        
        return status
    
    def _handle_suggestion_request(self, command: str) -> Dict[str, Any]:
        """Handle suggestion/recommendation request"""
        
        suggestions = learning_system.make_suggestion(command)
        
        print("\n💡 Suggestions:")
        for i, suggestion in enumerate(suggestions['suggestions'], 1):
            print(f"  {i}. {suggestion['suggestion']}")
            print(f"     Reason: {suggestion['reason']}")
            print(f"     Confidence: {suggestion['confidence']*100:.0f}%")
        
        return {
            'success': True,
            'suggestions': suggestions
        }
    
    def _handle_help_request(self) -> Dict[str, Any]:
        """Handle help request"""
        
        help_text = f"""
🔮 {self.name} - Complete Autonomous System

Available Commands:

📝 CODE GENERATION:
  - "Create a Python website"
  - "Build an e-commerce app"
  - "Generate API server in JavaScript"
  - "Make a mobile app"

🎨 DESIGN GENERATION:
  - "Create a logo"
  - "Design a UI/UX"
  - "Generate brand identity"
  - "Make a color scheme"

📊 SYSTEM STATUS:
  - "Show status"
  - "What's my progress?"
  - "System info"

💡 SUGGESTIONS:
  - "Give me suggestions"
  - "What should I build?"
  - "Recommend something"

🆘 HELP:
  - "Help"
  - "What can you do?"

🌟 FEATURES:
  ✓ Voice Learning & Recognition
  ✓ Unlimited Code Generation
  ✓ Auto Design Generation
  ✓ Offline Capabilities
  ✓ Military-Grade Encryption
  ✓ Continuous Learning & Adaptation
  ✓ Complete Autonomy

🔒 SECURITY:
  ✓ All data encrypted with {config.ENCRYPTION_ALGORITHM}
  ✓ Hidden vault accessible only to you
  ✓ No third-party access
  ✓ Complete privacy guaranteed

Current Phase: {voice_learning_system.current_phase}
Total Interactions: {learning_system.learning_stats['total_interactions']}
"""
        
        print(help_text)
        
        return {
            'success': True,
            'message': help_text
        }
    
    def _extract_language(self, command: str) -> str:
        """Extract programming language from command"""
        command_lower = command.lower()
        
        for lang in config.SUPPORTED_LANGUAGES:
            if lang.lower() in command_lower:
                return lang
        
        # Default to Python
        return 'Python'
    
    def _extract_project_type(self, command: str) -> Optional[str]:
        """Extract project type from command"""
        command_lower = command.lower()
        
        for proj_type in config.PROJECT_TYPES:
            if proj_type.lower() in command_lower:
                return proj_type
        
        # Try to infer
        if 'website' in command_lower or 'web' in command_lower:
            return 'Website'
        elif 'api' in command_lower:
            return 'API Server'
        elif 'app' in command_lower:
            return 'Mobile App'
        
        return None
    
    def _extract_design_type(self, command: str) -> str:
        """Extract design type from command"""
        command_lower = command.lower()
        
        for design_type in config.DESIGN_CATEGORIES:
            if design_type.lower() in command_lower:
                return design_type
        
        # Default to UI/UX
        return 'UI/UX'
    
    def _log_activity(self, activity_type: str, details: Any):
        """Log activity for tracking"""
        self.activity_log.append({
            'type': activity_type,
            'details': details,
            'timestamp': datetime.now().isoformat()
        })
    
    def get_system_info(self) -> Dict[str, Any]:
        """Get complete system information"""
        return {
            'name': self.name,
            'version': self.version,
            'user': self.user_name,
            'initialized': self.initialized,
            'features': config.FEATURES,
            'permissions': config.PERMISSIONS,
            'supported_languages': config.SUPPORTED_LANGUAGES,
            'project_types': config.PROJECT_TYPES,
            'design_categories': config.DESIGN_CATEGORIES,
            'security_level': config.SECURITY_LEVEL,
            'offline_mode': config.OFFLINE_MODE
        }
    
    def shutdown(self):
        """Graceful shutdown"""
        print(f"\n👋 Shutting down {self.name}...")
        print(f"  Total activities logged: {len(self.activity_log)}")
        print(f"  All data encrypted and stored securely")
        print(f"  Thank you, {self.user_name}!")


# Create global AMRIT AI instance
amrit = AmritAI()


if __name__ == '__main__':
    print("\n" + "="*60)
    print(f"  {config.SYSTEM_NAME}")
    print(f"  {config.SYSTEM_DESCRIPTION}")
    print("="*60)
    
    # Show system info
    info = amrit.get_system_info()
    print(f"\n✨ System ready for {info['user']}!")
    print(f"🔐 Security Level: {info['security_level']}")
    print(f"📴 Offline Mode: {'Enabled' if info['offline_mode'] else 'Disabled'}")
    
    print("\n💬 Try commands like:")
    print("  - amrit.process_voice_command('Create a Python website')")
    print("  - amrit.process_voice_command('Design a logo')")
    print("  - amrit.process_voice_command('Show status')")
    print("  - amrit.process_voice_command('Help')")
