"""
AMRIT AI Voice Learning System
Handles voice recognition, pattern learning, and user identification
"""

import json
from datetime import datetime
from typing import Dict, List, Optional, Any
import amrit_config as config
from secure_storage import secure_storage
from encryption_manager import encryption_manager


class VoiceLearningSystem:
    """
    Voice learning and recognition system for AMRIT AI
    Learns user's voice patterns and preferences over time
    """
    
    def __init__(self):
        self.current_phase = 'RECOGNITION'
        self.samples_collected = 0
        self.user_identified = False
        self.voice_profile = None
        self._load_voice_profile()
    
    def _load_voice_profile(self):
        """Load existing voice profile if available"""
        voice_prefs = secure_storage.load_preference('voice_profile')
        if voice_prefs:
            self.voice_profile = voice_prefs
            self.samples_collected = voice_prefs.get('samples_count', 0)
            self.user_identified = voice_prefs.get('user_identified', False)
            self.current_phase = self._determine_phase()
    
    def _determine_phase(self) -> str:
        """Determine current learning phase based on samples collected"""
        for phase_name, phase_info in config.VOICE_LEARNING_PHASES.items():
            if self.samples_collected < phase_info['samples_required']:
                return phase_name
        return 'MASTERY'
    
    def record_voice_sample(self, audio_data: bytes, context: Optional[str] = None) -> Dict[str, Any]:
        """
        Record and process a voice sample
        
        Args:
            audio_data: Raw audio data (in real implementation, would be actual audio)
            context: Context of the voice command (optional)
        
        Returns:
            Processing result with learning status
        """
        # In a real implementation, this would:
        # 1. Process actual audio data
        # 2. Extract voice features (pitch, tone, cadence, etc.)
        # 3. Compare with existing patterns
        # 4. Update learning model
        
        sample_data = {
            'audio_hash': encryption_manager.hash_data(str(audio_data)),
            'context': context,
            'timestamp': datetime.now().isoformat(),
            'phase': self.current_phase,
            'sample_number': self.samples_collected + 1
        }
        
        # Save biometric data
        biometric_id = secure_storage.save_voice_biometric(sample_data)
        
        # Update counters
        self.samples_collected += 1
        
        # Update phase if threshold reached
        old_phase = self.current_phase
        self.current_phase = self._determine_phase()
        
        # Update voice profile
        self._update_voice_profile()
        
        result = {
            'success': True,
            'biometric_id': biometric_id,
            'sample_number': self.samples_collected,
            'current_phase': self.current_phase,
            'phase_changed': old_phase != self.current_phase,
            'progress_percentage': self._calculate_progress(),
            'message': self._get_phase_message()
        }
        
        return result
    
    def _update_voice_profile(self):
        """Update and save voice profile"""
        if not self.voice_profile:
            self.voice_profile = {}
        
        self.voice_profile.update({
            'user_name': config.USER_NAME,
            'samples_count': self.samples_collected,
            'current_phase': self.current_phase,
            'user_identified': self.samples_collected >= config.VOICE_LEARNING_PHASES['RECOGNITION']['samples_required'],
            'last_updated': datetime.now().isoformat()
        })
        
        secure_storage.save_preference('voice_profile', self.voice_profile)
        self.user_identified = self.voice_profile['user_identified']
    
    def _calculate_progress(self) -> float:
        """Calculate overall learning progress percentage"""
        total_samples_for_mastery = config.VOICE_LEARNING_PHASES['MASTERY']['samples_required']
        progress = (self.samples_collected / total_samples_for_mastery) * 100
        return min(progress, 100.0)
    
    def _get_phase_message(self) -> str:
        """Get appropriate message for current phase"""
        messages = {
            'RECOGNITION': f"सीख रहा हूँ आपकी आवाज़ को... {self.samples_collected} samples collected. Recognition phase में हैं।",
            'LEARNING': f"आपकी preferences सीख रहा हूँ... {self.samples_collected} samples collected. Learning phase में हैं।",
            'ADAPTATION': f"आपके साथ adapt कर रहा हूँ... {self.samples_collected} samples collected. Adaptation phase में हैं।",
            'MASTERY': f"आपको पूरी तरह समझ चुका हूँ! {self.samples_collected} samples collected. Mastery achieved!"
        }
        return messages.get(self.current_phase, "Learning in progress...")
    
    def recognize_user(self, audio_data: bytes) -> Dict[str, Any]:
        """
        Recognize user from voice sample
        
        Args:
            audio_data: Audio data to identify
        
        Returns:
            Recognition result
        """
        # In real implementation, would use ML model to match voice patterns
        
        if not self.user_identified:
            return {
                'identified': False,
                'confidence': 0.0,
                'message': 'अभी आपकी आवाज़ सीख रहा हूँ। थोड़ा और समय लगेगा।'
            }
        
        # Simulate recognition
        return {
            'identified': True,
            'user_name': config.USER_NAME,
            'confidence': 0.95,
            'message': f'नमस्ते {config.USER_NAME}! आपको पहचान लिया।'
        }
    
    def learn_preference_from_voice(self, command: str, feedback: Optional[str] = None):
        """
        Learn user preferences from voice commands and feedback
        
        Args:
            command: Voice command given
            feedback: User feedback (optional)
        """
        pattern_data = {
            'command': command,
            'feedback': feedback,
            'phase': self.current_phase
        }
        
        secure_storage.save_learned_pattern('voice_commands', pattern_data)
    
    def get_voice_statistics(self) -> Dict[str, Any]:
        """Get voice learning statistics"""
        return {
            'user_name': config.USER_NAME,
            'current_phase': self.current_phase,
            'samples_collected': self.samples_collected,
            'user_identified': self.user_identified,
            'progress_percentage': self._calculate_progress(),
            'next_phase': self._get_next_phase(),
            'samples_until_next_phase': self._get_samples_until_next_phase()
        }
    
    def _get_next_phase(self) -> Optional[str]:
        """Get next learning phase"""
        phases = list(config.VOICE_LEARNING_PHASES.keys())
        current_index = phases.index(self.current_phase)
        if current_index < len(phases) - 1:
            return phases[current_index + 1]
        return None
    
    def _get_samples_until_next_phase(self) -> int:
        """Get number of samples needed for next phase"""
        next_phase = self._get_next_phase()
        if not next_phase:
            return 0
        
        required = config.VOICE_LEARNING_PHASES[next_phase]['samples_required']
        return max(0, required - self.samples_collected)


# Global voice learning system instance
voice_learning_system = VoiceLearningSystem()
