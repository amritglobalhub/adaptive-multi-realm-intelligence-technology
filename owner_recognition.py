"""
AMRIT AI - Owner Recognition Module

Multi-modal biometric verification system for owner identification.
Includes voice print analysis, speech pattern recognition, and behavioral signatures.
"""

import numpy as np
from typing import Dict, Optional, Tuple, List
from datetime import datetime
import hashlib
import config
from hidden_storage import HiddenStorageManager


class BiometricProfile:
    """Stores biometric characteristics of the owner"""
    
    def __init__(self):
        self.voice_features = {}
        self.speech_patterns = {}
        self.behavioral_patterns = {}
        self.created_at = datetime.now().isoformat()
        self.last_updated = datetime.now().isoformat()
        self.sample_count = 0
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for storage"""
        return {
            'voice_features': self.voice_features,
            'speech_patterns': self.speech_patterns,
            'behavioral_patterns': self.behavioral_patterns,
            'created_at': self.created_at,
            'last_updated': self.last_updated,
            'sample_count': self.sample_count
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """Create from dictionary"""
        profile = cls()
        profile.voice_features = data.get('voice_features', {})
        profile.speech_patterns = data.get('speech_patterns', {})
        profile.behavioral_patterns = data.get('behavioral_patterns', {})
        profile.created_at = data.get('created_at', datetime.now().isoformat())
        profile.last_updated = data.get('last_updated', datetime.now().isoformat())
        profile.sample_count = data.get('sample_count', 0)
        return profile


class OwnerRecognitionEngine:
    """Multi-modal owner recognition and verification"""
    
    def __init__(self, storage_manager: HiddenStorageManager):
        """
        Initialize owner recognition engine
        
        Args:
            storage_manager: Hidden storage manager instance
        """
        self.storage = storage_manager
        self.owner_profile = None
        self.failed_attempts = 0
        self.locked_until = None
        self._load_profile()
    
    def _load_profile(self):
        """Load owner profile from storage"""
        try:
            profile_data = self.storage.retrieve_data(
                'personal_biometrics',
                'owner_profile'
            )
            if profile_data:
                self.owner_profile = BiometricProfile.from_dict(profile_data)
        except:
            self.owner_profile = None
    
    def _save_profile(self):
        """Save owner profile to storage"""
        if self.owner_profile:
            self.storage.store_data(
                'personal_biometrics',
                'owner_profile',
                self.owner_profile.to_dict()
            )
    
    def is_locked(self) -> bool:
        """Check if authentication is currently locked"""
        if self.locked_until:
            if datetime.now() < self.locked_until:
                return True
            else:
                self.locked_until = None
                self.failed_attempts = 0
        return False
    
    def extract_voice_features(self, audio_data: np.ndarray, 
                              sample_rate: int = 16000) -> Dict:
        """
        Extract voice features from audio data
        
        Args:
            audio_data: Audio samples as numpy array
            sample_rate: Sample rate in Hz
            
        Returns:
            Dictionary of voice features
        """
        # Placeholder for voice feature extraction
        # In production, would use librosa, pyannote, etc.
        
        features = {
            'mfcc_mean': np.mean(audio_data).tolist() if len(audio_data) > 0 else 0,
            'mfcc_std': np.std(audio_data).tolist() if len(audio_data) > 0 else 0,
            'pitch_mean': 0.0,  # Placeholder
            'pitch_std': 0.0,   # Placeholder
            'energy_mean': np.mean(np.abs(audio_data)).tolist() if len(audio_data) > 0 else 0,
            'zero_crossing_rate': 0.0,  # Placeholder
            'spectral_centroid': 0.0,  # Placeholder
            'tempo': 0.0,  # Placeholder
        }
        
        return features
    
    def extract_speech_patterns(self, text: str) -> Dict:
        """
        Extract speech patterns from transcribed text
        
        Args:
            text: Transcribed speech text
            
        Returns:
            Dictionary of speech patterns
        """
        words = text.lower().split()
        
        patterns = {
            'word_count': len(words),
            'unique_words': len(set(words)),
            'avg_word_length': np.mean([len(w) for w in words]) if words else 0,
            'sentence_count': text.count('.') + text.count('!') + text.count('?'),
            'vocabulary_richness': len(set(words)) / len(words) if words else 0,
            'common_words': {},  # Could track frequently used words
            'speaking_style': 'formal',  # Placeholder for style classification
        }
        
        return patterns
    
    def extract_behavioral_signature(self, interaction_data: Dict) -> Dict:
        """
        Extract behavioral signature from interaction
        
        Args:
            interaction_data: Dictionary with interaction metadata
            
        Returns:
            Dictionary of behavioral features
        """
        signature = {
            'time_of_day': interaction_data.get('timestamp', ''),
            'interaction_duration': interaction_data.get('duration', 0),
            'command_type': interaction_data.get('command_type', ''),
            'typing_speed': interaction_data.get('typing_speed', 0),
            'pause_patterns': interaction_data.get('pauses', []),
            'context_switches': interaction_data.get('context_switches', 0),
        }
        
        return signature
    
    def enroll_owner(self, audio_samples: List[np.ndarray], 
                    text_samples: List[str],
                    behavioral_data: List[Dict]) -> bool:
        """
        Enroll owner with multiple biometric samples
        
        Args:
            audio_samples: List of audio sample arrays
            text_samples: List of transcribed text samples
            behavioral_data: List of behavioral interaction data
            
        Returns:
            True if enrollment successful
        """
        try:
            # Create new profile
            self.owner_profile = BiometricProfile()
            
            # Extract and average voice features
            voice_features_list = []
            for audio in audio_samples:
                features = self.extract_voice_features(audio)
                voice_features_list.append(features)
            
            # Average voice features
            if voice_features_list:
                self.owner_profile.voice_features = {
                    key: np.mean([f[key] for f in voice_features_list])
                    for key in voice_features_list[0].keys()
                }
            
            # Extract and combine speech patterns
            for text in text_samples:
                patterns = self.extract_speech_patterns(text)
                for key, value in patterns.items():
                    if key not in self.owner_profile.speech_patterns:
                        self.owner_profile.speech_patterns[key] = []
                    self.owner_profile.speech_patterns[key].append(value)
            
            # Extract and combine behavioral patterns
            for data in behavioral_data:
                signature = self.extract_behavioral_signature(data)
                for key, value in signature.items():
                    if key not in self.owner_profile.behavioral_patterns:
                        self.owner_profile.behavioral_patterns[key] = []
                    self.owner_profile.behavioral_patterns[key].append(value)
            
            self.owner_profile.sample_count = len(audio_samples)
            self.owner_profile.last_updated = datetime.now().isoformat()
            
            # Save profile
            self._save_profile()
            
            return True
        
        except Exception as e:
            print(f"Error during enrollment: {e}")
            return False
    
    def verify_owner(self, audio_data: Optional[np.ndarray] = None,
                    text: Optional[str] = None,
                    behavioral_data: Optional[Dict] = None) -> Tuple[bool, float]:
        """
        Verify if current user is the owner
        
        Args:
            audio_data: Optional audio sample
            text: Optional transcribed text
            behavioral_data: Optional behavioral data
            
        Returns:
            Tuple of (is_owner, confidence_score)
        """
        if self.is_locked():
            return False, 0.0
        
        if not self.owner_profile:
            return False, 0.0
        
        scores = []
        
        # Voice verification
        if audio_data is not None:
            voice_features = self.extract_voice_features(audio_data)
            voice_score = self._compare_voice_features(voice_features)
            scores.append(('voice', voice_score))
        
        # Speech pattern verification
        if text is not None:
            speech_patterns = self.extract_speech_patterns(text)
            speech_score = self._compare_speech_patterns(speech_patterns)
            scores.append(('speech', speech_score))
        
        # Behavioral verification
        if behavioral_data is not None:
            behavioral_sig = self.extract_behavioral_signature(behavioral_data)
            behavioral_score = self._compare_behavioral_patterns(behavioral_sig)
            scores.append(('behavioral', behavioral_score))
        
        if not scores:
            return False, 0.0
        
        # Calculate weighted average
        total_score = sum(score for _, score in scores) / len(scores)
        
        # Apply thresholds
        is_owner = total_score >= config.OVERALL_CONFIDENCE_THRESHOLD
        
        # Update failed attempts
        if not is_owner:
            self.failed_attempts += 1
            if self.failed_attempts >= config.MAX_FAILED_AUTH_ATTEMPTS:
                from datetime import timedelta
                self.locked_until = datetime.now() + timedelta(
                    seconds=config.AUTH_LOCKOUT_TIME
                )
        else:
            self.failed_attempts = 0
        
        return is_owner, total_score
    
    def _compare_voice_features(self, features: Dict) -> float:
        """Compare voice features with stored profile"""
        if not self.owner_profile.voice_features:
            return 0.0
        
        # Simple euclidean distance comparison
        # In production, would use more sophisticated ML models
        distances = []
        for key in features.keys():
            if key in self.owner_profile.voice_features:
                stored_val = self.owner_profile.voice_features[key]
                current_val = features[key]
                if isinstance(stored_val, (int, float)) and isinstance(current_val, (int, float)):
                    distances.append(abs(stored_val - current_val))
        
        if not distances:
            return 0.5
        
        # Convert distance to similarity score (0-1)
        avg_distance = np.mean(distances)
        similarity = 1.0 / (1.0 + avg_distance)
        
        return similarity
    
    def _compare_speech_patterns(self, patterns: Dict) -> float:
        """Compare speech patterns with stored profile"""
        if not self.owner_profile.speech_patterns:
            return 0.0
        
        # Simple pattern matching
        matches = 0
        total = 0
        
        for key, value in patterns.items():
            if key in self.owner_profile.speech_patterns:
                stored_values = self.owner_profile.speech_patterns[key]
                if stored_values:
                    # Compare with average of stored values
                    if isinstance(value, (int, float)):
                        avg_stored = np.mean(stored_values)
                        similarity = 1.0 / (1.0 + abs(avg_stored - value))
                        matches += similarity
                    total += 1
        
        return matches / total if total > 0 else 0.5
    
    def _compare_behavioral_patterns(self, signature: Dict) -> float:
        """Compare behavioral patterns with stored profile"""
        if not self.owner_profile.behavioral_patterns:
            return 0.0
        
        # Simple behavioral matching
        matches = 0
        total = 0
        
        for key, value in signature.items():
            if key in self.owner_profile.behavioral_patterns:
                stored_values = self.owner_profile.behavioral_patterns[key]
                if stored_values and value:
                    # Basic comparison
                    matches += 0.5  # Placeholder
                total += 1
        
        return matches / total if total > 0 else 0.5
    
    def detect_spoofing(self, audio_data: np.ndarray) -> Tuple[bool, float]:
        """
        Detect if audio sample is potentially spoofed/synthetic
        
        Args:
            audio_data: Audio sample to analyze
            
        Returns:
            Tuple of (is_spoofed, confidence)
        """
        # Placeholder for spoofing detection
        # In production, would use anti-spoofing models
        
        # Simple check: look for unnatural patterns
        if len(audio_data) == 0:
            return True, 1.0
        
        # Check for repeating patterns (simple synthetic voice indicator)
        energy = np.abs(audio_data)
        variance = np.var(energy)
        
        # Very low variance could indicate synthetic audio
        if variance < 0.001:
            return True, 0.8
        
        return False, 0.1
    
    def update_profile(self, audio_data: Optional[np.ndarray] = None,
                      text: Optional[str] = None,
                      behavioral_data: Optional[Dict] = None):
        """
        Update owner profile with new verified samples
        
        Args:
            audio_data: Optional audio sample
            text: Optional transcribed text
            behavioral_data: Optional behavioral data
        """
        if not self.owner_profile:
            return
        
        try:
            if audio_data is not None:
                new_features = self.extract_voice_features(audio_data)
                # Update with exponential moving average
                alpha = 0.1  # Learning rate
                for key, value in new_features.items():
                    if key in self.owner_profile.voice_features:
                        old_value = self.owner_profile.voice_features[key]
                        self.owner_profile.voice_features[key] = (
                            alpha * value + (1 - alpha) * old_value
                        )
                    else:
                        self.owner_profile.voice_features[key] = value
            
            self.owner_profile.sample_count += 1
            self.owner_profile.last_updated = datetime.now().isoformat()
            self._save_profile()
        
        except Exception as e:
            print(f"Error updating profile: {e}")
    
    def get_profile_stats(self) -> Dict:
        """Get statistics about owner profile"""
        if not self.owner_profile:
            return {'enrolled': False}
        
        return {
            'enrolled': True,
            'created_at': self.owner_profile.created_at,
            'last_updated': self.owner_profile.last_updated,
            'sample_count': self.owner_profile.sample_count,
            'voice_features_count': len(self.owner_profile.voice_features),
            'speech_patterns_count': len(self.owner_profile.speech_patterns),
            'behavioral_patterns_count': len(self.owner_profile.behavioral_patterns),
        }
