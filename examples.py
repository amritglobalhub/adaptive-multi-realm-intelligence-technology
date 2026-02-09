"""
AMRIT AI - Comprehensive Usage Examples
Demonstrates all features of the iPhone Sync & Mobile Intelligence System
"""

from amrit_iphone_system import AMRITiPhoneSystem
import json


def example_1_basic_setup():
    """Example 1: Basic System Setup and iPhone Connection"""
    print("\n" + "="*60)
    print("Example 1: Basic Setup and iPhone Connection")
    print("="*60 + "\n")
    
    # Initialize system
    system = AMRITiPhoneSystem()
    init_result = system.initialize_system()
    
    print("✓ System initialized")
    print(f"  - Core active: {init_result['core_active']}")
    print(f"  - Voice interface: {init_result['voice_interface_active']}")
    print(f"  - Offline mode: {init_result['offline_mode_enabled']}")
    
    # Connect iPhone
    connect_result = system.connect_iphone("iPhone_001", "iPhone 15 Pro")
    
    print("\n✓ iPhone connected")
    print(f"  - Device: {connect_result['device']['device_name']}")
    print(f"  - Sync status: {connect_result['sync_result']['status']}")
    print(f"  - App activated: {connect_result['app_activation']['app_activated']}")
    
    return system


def example_2_voice_interaction(system):
    """Example 2: Voice Input and Intelligent Questioning"""
    print("\n" + "="*60)
    print("Example 2: Voice Input and Intelligent Questioning")
    print("="*60 + "\n")
    
    # Short voice input
    print("User: मुझे एक mobile app चाहिए")
    result = system.process_user_voice_input("मुझे एक mobile app चाहिए")
    print(f"AMRIT: {result['voice_processing']['voice_response']}\n")
    
    # Long-form voice input
    long_input = """
    मुझे एक e-commerce platform चाहिए जिसमें:
    - Product catalog with search
    - Shopping cart functionality
    - Payment gateway integration (Stripe/PayPal)
    - User authentication and profiles
    - Order tracking
    - Admin dashboard
    - Mobile responsive design
    - Push notifications
    """
    
    print("User: [Long detailed requirements about e-commerce platform]")
    result = system.process_user_voice_input(long_input, is_long_form=True)
    
    if result['voice_processing'].get('followup_questions'):
        print("\nAMRIT asks clarifying questions:")
        for i, q in enumerate(result['voice_processing']['followup_questions'], 1):
            print(f"  {i}. {q}")


def example_3_permission_management(system):
    """Example 3: Permission Management with Voice"""
    print("\n" + "="*60)
    print("Example 3: Permission Management")
    print("="*60 + "\n")
    
    # Request code generation permission
    request = system.permission_manager.request_permission("code_generation")
    print(f"AMRIT: {request['voice_prompt']}")
    
    response = system.grant_permission_by_voice("code_generation", "हाँ, करो")
    print(f"User: हाँ, करो")
    print(f"Result: {response['message']}\n")
    
    # Request learning permission with full access
    request = system.permission_manager.request_permission("learning_preferences")
    print(f"AMRIT: {request['voice_prompt']}")
    
    response = system.grant_permission_by_voice("learning_preferences", "पूरी तरह, सब कुछ सीख")
    print(f"User: पूरी तरह, सब कुछ सीख")
    print(f"Result: {response['message']}")
    print(f"Access Level: {response['access_level']}\n")
    
    # Check permission status
    all_perms = system.permission_manager.get_all_permissions()
    granted = [p['name'] for p in all_perms.values() if p['granted']]
    print(f"✓ Granted permissions: {', '.join(granted)}")


def example_4_code_generation(system):
    """Example 4: Code Generation on iPhone"""
    print("\n" + "="*60)
    print("Example 4: Code Generation on iPhone")
    print("="*60 + "\n")
    
    # Request code generation
    requirements = "Authentication system with JWT tokens and password hashing"
    code_gen = system.generate_code_on_iphone(requirements)
    
    print(f"AMRIT: {code_gen['confirmation']['voice_prompt']}")
    print("User: हाँ, बहुत अच्छा है\n")
    
    # Execute code generation
    exec_result = system.execute_code_generation(
        code_gen['confirmation']['confirmation_id'],
        "हाँ, बहुत अच्छा है",
        requirements
    )
    
    if exec_result['status'] == 'success':
        print("✓ Code generated successfully")
        print(f"  - Generated on: {exec_result['code']['generated_on']}")
        print(f"  - Language: {exec_result['code']['language']}")
        print(f"  - Encrypted: {exec_result['code']['encrypted']}")
        print(f"\nGenerated Code Preview:")
        print("-" * 50)
        print(exec_result['code']['code'][:200] + "...")


def example_5_offline_mode(system):
    """Example 5: Offline Development"""
    print("\n" + "="*60)
    print("Example 5: Offline Mode and Local Storage")
    print("="*60 + "\n")
    
    # Enable offline mode
    offline_status = system.offline_mode.enable_offline_mode()
    print(f"✓ Offline mode: {offline_status['offline_mode']}")
    print(f"✓ Full functionality: {offline_status['full_functionality']}\n")
    
    # Store data offline
    project_data = {
        "name": "AMRIT Mobile App",
        "version": "1.0.0",
        "features": ["Voice", "Sync", "Offline"],
        "status": "in_development"
    }
    
    store_result = system.offline_mode.store_locally("project_data", project_data)
    print(f"✓ Data stored locally")
    print(f"  - Key: {store_result['key']}")
    print(f"  - Pending sync: {store_result['pending_sync']}\n")
    
    # Check offline status
    status = system.offline_mode.get_offline_status()
    print(f"Offline Status:")
    print(f"  - Enabled: {status['offline_enabled']}")
    print(f"  - Local items: {status['local_items']}")
    print(f"  - Pending sync: {status['pending_sync']}")
    print(f"  - Storage used: {status['storage_used']} bytes")


def example_6_iphone_features(system):
    """Example 6: iPhone-Specific Features"""
    print("\n" + "="*60)
    print("Example 6: iPhone-Specific Features")
    print("="*60 + "\n")
    
    # Code generation
    code_result = system.iphone_features.generate_code_on_iphone(
        "REST API with authentication"
    )
    print(f"✓ Code Generation: {code_result['status']}")
    print(f"  - Generated on: {code_result['generated_on']}")
    print(f"  - Encrypted: {code_result['encrypted']}\n")
    
    # Design creation
    design_result = system.iphone_features.create_design_on_iphone(
        "Modern dashboard with dark mode"
    )
    print(f"✓ Design Creation: {design_result['status']}")
    print(f"  - Type: {design_result['design_type']}")
    print(f"  - Dark mode: {design_result['dark_mode']}")
    print(f"  - Components: {', '.join(design_result['components'])}\n")
    
    # Project management
    project_result = system.iphone_features.manage_project_on_iphone(
        "AMRIT AI Mobile",
        "create"
    )
    print(f"✓ Project Management: {project_result['status']}")
    print(f"  - {project_result['message']}\n")
    
    # Voice notes
    note_result = system.iphone_features.record_voice_note(
        "Requirements discussion for new feature",
        duration=180
    )
    print(f"✓ Voice Note Recorded: {note_result['status']}")
    print(f"  - Note ID: {note_result['note_id']}")
    print(f"  - Duration: {note_result['duration_seconds']}s")
    print(f"  - Encrypted: {note_result['encrypted']}\n")
    
    # Quick shortcuts
    print("Quick Access Shortcuts:")
    shortcuts = system.iphone_features.get_quick_shortcuts()
    for shortcut in shortcuts:
        print(f"  {shortcut['name']}")


def example_7_data_sync(system):
    """Example 7: Data Synchronization"""
    print("\n" + "="*60)
    print("Example 7: Data Synchronization")
    print("="*60 + "\n")
    
    # Perform sync
    sync_result = system.sync_data()
    
    print(f"✓ Sync completed: {sync_result['status']}")
    print(f"\nSync Steps:")
    for i, step in enumerate(sync_result['sync_result']['sync_steps'], 1):
        print(f"  {i}. {step}")
    
    print(f"\nOffline Sync:")
    print(f"  - Synced items: {sync_result['offline_sync']['synced_count']}")


def example_8_conversation_flow(system):
    """Example 8: Natural Conversation Flow"""
    print("\n" + "="*60)
    print("Example 8: Natural Conversation Flow")
    print("="*60 + "\n")
    
    # Simulate a natural conversation
    conversation = [
        {
            "speaker": "user",
            "message": "मुझे privacy-focused social media app चाहिए",
            "is_long": False
        },
        {
            "speaker": "user",
            "message": "हाँ, end-to-end encrypted messages",
            "is_long": False
        },
        {
            "speaker": "user",
            "message": "local storage भी चाहिए offline mode के लिए",
            "is_long": False
        }
    ]
    
    print("Natural Conversation Example:")
    print("-" * 50)
    
    for turn in conversation:
        print(f"\nUser: {turn['message']}")
        result = system.process_user_voice_input(turn['message'], turn['is_long'])
        print(f"AMRIT: {result['voice_processing']['voice_response']}")
    
    print("\n✓ Conversation flow maintained with context preservation")


def example_9_system_status(system):
    """Example 9: System Status and Monitoring"""
    print("\n" + "="*60)
    print("Example 9: System Status and Monitoring")
    print("="*60 + "\n")
    
    # Get complete system status
    status = system.get_system_status()
    
    print("System Status Report:")
    print("-" * 50)
    print(f"System Active: {status['system_active']}")
    print(f"Core Status: {status['core_status']}")
    
    if status['connected_device']:
        print(f"\nConnected Device:")
        print(f"  - Name: {status['connected_device']['device_name']}")
        print(f"  - ID: {status['connected_device']['device_id']}")
        print(f"  - Connected: {status['connected_device']['connected']}")
        print(f"  - Sync Status: {status['connected_device']['sync_status']}")
    
    print(f"\nVoice Interface: {status['voice_interface_active']}")
    print(f"Permissions Granted: {status['permissions_granted']}")
    
    print(f"\nOffline Mode:")
    print(f"  - Enabled: {status['offline_mode']['offline_enabled']}")
    print(f"  - Local items: {status['offline_mode']['local_items']}")
    print(f"  - Pending sync: {status['offline_mode']['pending_sync']}")
    
    print(f"\niPhone App Status:")
    for key, value in status['iphone_app_status'].items():
        print(f"  - {key}: {value}")


def main():
    """Run all examples"""
    print("\n" + "="*80)
    print("  🍎 AMRIT AI - Comprehensive Usage Examples")
    print("  iPhone Sync & Mobile Intelligence System")
    print("="*80)
    
    # Example 1: Setup
    system = example_1_basic_setup()
    
    # Example 2: Voice Interaction
    example_2_voice_interaction(system)
    
    # Example 3: Permission Management
    example_3_permission_management(system)
    
    # Example 4: Code Generation
    example_4_code_generation(system)
    
    # Example 5: Offline Mode
    example_5_offline_mode(system)
    
    # Example 6: iPhone Features
    example_6_iphone_features(system)
    
    # Example 7: Data Sync
    example_7_data_sync(system)
    
    # Example 8: Conversation Flow
    example_8_conversation_flow(system)
    
    # Example 9: System Status
    example_9_system_status(system)
    
    print("\n" + "="*80)
    print("  ✅ All Examples Completed Successfully!")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
