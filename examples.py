"""
AMRIT AI - Example Usage Script

Demonstrates various features of the AMRIT AI system.
"""

import numpy as np
from datetime import datetime
from amrit_system import AMRITSystem
from permission_manager import PermissionType


def example_enrollment():
    """Example: First-time owner enrollment"""
    print("\n" + "="*60)
    print("Example 1: Owner Enrollment")
    print("="*60 + "\n")
    
    # Initialize system
    system = AMRITSystem("demo_password_123")
    
    # Prepare enrollment samples (in production, these would be real audio/text)
    print("Preparing enrollment samples...")
    audio_samples = [np.random.randn(16000) for _ in range(5)]
    text_samples = [
        "Hello AMRIT, this is my voice",
        "Initialize learning system",
        "I prefer detailed responses",
        "Start personalization",
        "Thank you AMRIT"
    ]
    behavioral_samples = [
        {'timestamp': datetime.now().isoformat(), 'duration': 10, 'typing_speed': 45},
        {'timestamp': datetime.now().isoformat(), 'duration': 15, 'typing_speed': 42},
        {'timestamp': datetime.now().isoformat(), 'duration': 12, 'typing_speed': 48},
        {'timestamp': datetime.now().isoformat(), 'duration': 14, 'typing_speed': 44},
        {'timestamp': datetime.now().isoformat(), 'duration': 11, 'typing_speed': 46},
    ]
    
    # Enroll owner
    success = system.enroll_owner(audio_samples, text_samples, behavioral_samples)
    
    if success:
        print("\n✅ Owner enrolled successfully!")
        print("   Now you can authenticate using your biometric data")
    
    system.end_session()


def example_authentication():
    """Example: Owner authentication"""
    print("\n" + "="*60)
    print("Example 2: Owner Authentication")
    print("="*60 + "\n")
    
    system = AMRITSystem("demo_password_123")
    
    # Authenticate with voice and text
    print("Authenticating with biometric data...")
    audio = np.random.randn(16000)  # Voice sample
    text = "Hello AMRIT"
    behavioral = {'timestamp': datetime.now().isoformat(), 'duration': 10}
    
    authenticated = system.authenticate_owner(
        audio_data=audio,
        text=text,
        behavioral_data=behavioral
    )
    
    if authenticated:
        print("✅ Authentication successful!")
        print("   Session is now active")
        system.print_status()
    
    system.end_session()


def example_learning():
    """Example: Self-learning from interactions"""
    print("\n" + "="*60)
    print("Example 3: Self-Learning System")
    print("="*60 + "\n")
    
    system = AMRITSystem("demo_password_123")
    
    # Authenticate
    audio = np.random.randn(16000)
    system.authenticate_owner(audio_data=audio, text="Hello")
    
    # Record various interactions
    print("Recording interactions for learning...")
    
    interactions = [
        ('command', {
            'command': 'analyze_data',
            'context': {'dataset': 'sales_2024'},
            'success': True
        }),
        ('query', {
            'query': 'what are the trends in Q1',
            'response': 'Sales increased by 15% in Q1...',
            'satisfaction': 0.9
        }),
        ('conversation', {
            'text': 'I prefer concise summaries with key metrics highlighted'
        }),
        ('preference', {
            'type': 'response_style',
            'value': 'brief_with_examples'
        }),
        ('command', {
            'command': 'generate_report',
            'context': {'format': 'pdf', 'sections': ['summary', 'charts']},
            'success': True
        })
    ]
    
    for interaction_type, data in interactions:
        system.record_interaction(interaction_type, data)
        print(f"  ✅ Recorded {interaction_type} interaction")
    
    # Get learned patterns
    print("\n📊 Learned Patterns:")
    patterns = system.get_learned_patterns()
    for pattern_type, pattern_data in patterns.items():
        print(f"  • {pattern_type}: {len(pattern_data)} patterns")
    
    # Get preferences
    print("\n🎯 Learned Preferences:")
    preferences = system.get_preferences()
    for pref_type, pref_data in preferences.items():
        print(f"  • {pref_type}")
    
    system.end_session()


def example_permissions():
    """Example: Permission-gated operations"""
    print("\n" + "="*60)
    print("Example 4: Permission System")
    print("="*60 + "\n")
    
    system = AMRITSystem("demo_password_123")
    
    # Authenticate
    audio = np.random.randn(16000)
    system.authenticate_owner(audio_data=audio, text="Hello")
    
    # Request permission for data modification
    print("Requesting permission for data modification...")
    request_id = system.request_permission(
        PermissionType.DATA_MODIFICATION,
        "Need to update user preference database"
    )
    
    # Grant permission
    print("\nGranting permission...")
    system.grant_permission(request_id, duration=3600)  # 1 hour
    
    # Check permission
    has_permission = system.permissions.check_permission(PermissionType.DATA_MODIFICATION)
    print(f"\n✅ Permission status: {'Granted' if has_permission else 'Denied'}")
    
    # Get permission statistics
    stats = system.permissions.get_statistics()
    print(f"\n📊 Permission Statistics:")
    print(f"  • Total requests: {stats['total_requests']}")
    print(f"  • Active permissions: {stats['active_permissions']}")
    
    system.end_session()


def example_data_mining():
    """Example: Data mining and analysis"""
    print("\n" + "="*60)
    print("Example 5: Data Mining Pipeline")
    print("="*60 + "\n")
    
    system = AMRITSystem("demo_password_123")
    
    # Authenticate
    audio = np.random.randn(16000)
    system.authenticate_owner(audio_data=audio, text="Hello")
    
    # Record sample interactions
    print("Recording sample data...")
    for i in range(20):
        system.record_interaction('command', {
            'command': f'action_{i % 5}',
            'context': {'index': i},
            'success': True
        })
    
    # Request and grant permission for analysis
    req_id = system.request_permission(
        PermissionType.DATA_MODIFICATION,
        "Running data analysis"
    )
    system.grant_permission(req_id)
    
    # Run analysis
    print("\nRunning data mining analysis...")
    insights = system.run_data_analysis()
    
    print("\n📊 Analysis Results:")
    print(f"  • Sample size: {insights.get('sample_size', 0)}")
    print(f"  • Command preferences found: {len(insights.get('command_preferences', {}).get('most_used', []))}")
    print(f"  • Time patterns identified: {len(insights.get('time_patterns', {}).get('active_hours', []))}")
    
    system.end_session()


def example_personalization():
    """Example: UI personalization generation"""
    print("\n" + "="*60)
    print("Example 6: Personalized UI Generation")
    print("="*60 + "\n")
    
    system = AMRITSystem("demo_password_123")
    
    # Authenticate
    audio = np.random.randn(16000)
    system.authenticate_owner(audio_data=audio, text="Hello")
    
    # Record interactions with preferences
    print("Learning user preferences...")
    preferences = [
        {'type': 'color_scheme', 'value': 'blue'},
        {'type': 'layout', 'value': 'compact'},
        {'type': 'font_size', 'value': 'medium'},
    ]
    
    for pref in preferences:
        system.record_interaction('preference', pref)
    
    # Request and grant permission for UI generation
    req_id = system.request_permission(
        PermissionType.SYSTEM_UPDATE,
        "Generating personalized UI"
    )
    system.grant_permission(req_id)
    
    # Generate personalized UI
    print("\nGenerating personalized UI...")
    ui_config = system.generate_personalized_ui()
    
    print("\n🎨 Generated UI Configuration:")
    if 'theme' in ui_config:
        print(f"  • Theme colors: {ui_config['theme'].get('primary', 'N/A')}")
    if 'dashboard' in ui_config:
        print(f"  • Dashboard widgets: {len(ui_config['dashboard'].get('widgets', []))}")
    if 'custom_commands' in ui_config:
        print(f"  • Custom commands: {len(ui_config['custom_commands'])}")
    
    system.end_session()


def run_all_examples():
    """Run all examples"""
    print("\n" + "="*80)
    print("🔮 AMRIT AI - Example Usage Demonstrations")
    print("="*80)
    
    try:
        example_enrollment()
        example_authentication()
        example_learning()
        example_permissions()
        example_data_mining()
        example_personalization()
        
        print("\n" + "="*80)
        print("✅ All examples completed successfully!")
        print("="*80 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    run_all_examples()
