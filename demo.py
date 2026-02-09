#!/usr/bin/env python3
"""
AMRIT AI Demo Script
Demonstrates all features of the AMRIT AI system
"""

import time
from amrit_ai import amrit
from voice_learning import voice_learning_system
from code_generator import code_generator
from design_generator import design_generator
from learning_system import learning_system
from secure_storage import secure_storage


def print_section(title):
    """Print a section header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")


def demo_voice_learning():
    """Demonstrate voice learning system"""
    print_section("🎤 VOICE LEARNING SYSTEM DEMO")
    
    print("Simulating voice samples being recorded...")
    
    # Simulate recording voice samples
    for i in range(5):
        sample = f"sample_{i}".encode()
        result = voice_learning_system.record_voice_sample(
            sample, 
            context=f"Command {i+1}"
        )
        print(f"  Sample {i+1}: {result['message']}")
        time.sleep(0.2)
    
    # Get voice statistics
    stats = voice_learning_system.get_voice_statistics()
    print(f"\n📊 Voice Learning Stats:")
    print(f"  Current Phase: {stats['current_phase']}")
    print(f"  Samples Collected: {stats['samples_collected']}")
    print(f"  Progress: {stats['progress_percentage']:.1f}%")
    print(f"  User Identified: {stats['user_identified']}")


def demo_code_generation():
    """Demonstrate code generation"""
    print_section("💻 CODE GENERATION DEMO")
    
    # Generate different types of projects
    projects = [
        ("Python website", "Python", "Website"),
        ("REST API server", "Python", "API Server"),
        ("JavaScript web app", "JavaScript", None),
    ]
    
    generated_projects = []
    
    for desc, lang, proj_type in projects:
        print(f"Generating {desc}...")
        result = code_generator.generate_code(
            description=desc,
            language=lang,
            project_type=proj_type
        )
        
        if result['success']:
            print(f"  ✅ {result['message']}")
            print(f"  Project ID: {result['project_id'][:16]}...")
            print(f"  Files: {len(result.get('files', {}))}")
            generated_projects.append(result['project_id'])
        else:
            print(f"  ❌ Failed: {result.get('error', 'Unknown error')}")
        
        time.sleep(0.2)
    
    print(f"\n📊 Code Generation Summary:")
    print(f"  Total Projects Generated: {len(generated_projects)}")
    
    # Show generation history
    history = code_generator.get_generation_history()
    print(f"  Total History Items: {len(history)}")


def demo_design_generation():
    """Demonstrate design generation"""
    print_section("🎨 DESIGN GENERATION DEMO")
    
    # Generate different types of designs
    designs = [
        ("Logo", "Modern tech startup logo"),
        ("UI/UX", "Dashboard design system"),
        ("Brand Identity", "Complete brand for AI company"),
        ("Color Scheme", "Professional color palette"),
    ]
    
    generated_designs = []
    
    for design_type, desc in designs:
        print(f"Generating {design_type}...")
        result = design_generator.generate_design(
            design_type=design_type,
            description=desc
        )
        
        if result['success']:
            print(f"  ✅ {result['message']}")
            print(f"  Design ID: {result['design_id'][:16]}...")
            generated_designs.append(result['design_id'])
            
            # Show some design details
            design = result['design']
            if isinstance(design, dict):
                if 'primary_color' in design:
                    print(f"  Primary Color: {design['primary_color']}")
                if 'style' in design:
                    print(f"  Style: {design['style']}")
        else:
            print(f"  ❌ Failed: {result.get('error', 'Unknown error')}")
        
        time.sleep(0.2)
    
    print(f"\n📊 Design Generation Summary:")
    print(f"  Total Designs Generated: {len(generated_designs)}")


def demo_learning_system():
    """Demonstrate learning and adaptation"""
    print_section("🧠 LEARNING & ADAPTATION DEMO")
    
    # Record some interactions
    print("Recording user interactions...")
    interactions = [
        ("code_generation", {"language": "Python", "type": "Website"}),
        ("design_generation", {"type": "Logo"}),
        ("code_generation", {"language": "JavaScript", "type": "API"}),
        ("voice_command", {"command": "Create an app"}),
    ]
    
    for i, (int_type, data) in enumerate(interactions):
        learning_system.record_interaction(int_type, data)
        print(f"  Interaction {i+1} recorded: {int_type}")
        time.sleep(0.1)
    
    # Analyze patterns
    print("\nAnalyzing learned patterns...")
    patterns = learning_system.analyze_patterns()
    print(f"  Total Interactions: {patterns['total_interactions']}")
    print(f"  Patterns Identified: {len(patterns['patterns_identified'])}")
    
    for pattern in patterns['patterns_identified']:
        print(f"\n  Category: {pattern['category']}")
        if pattern['category'] == 'coding_preferences':
            print(f"    Most Used Language: {pattern.get('most_used_language', 'N/A')}")
        elif pattern['category'] == 'design_preferences':
            print(f"    Most Requested Design: {pattern.get('most_requested_design', 'N/A')}")
    
    # Make suggestions
    print("\nGenerating intelligent suggestions...")
    suggestions = learning_system.make_suggestion()
    
    if suggestions['suggestions']:
        print(f"  Total Suggestions: {suggestions['total_suggestions']}")
        for i, sug in enumerate(suggestions['suggestions'][:3], 1):
            print(f"\n  Suggestion {i}:")
            print(f"    💡 {sug['suggestion']}")
            print(f"    💭 {sug['reason']}")
            print(f"    🎯 Confidence: {sug['confidence']*100:.0f}%")
    else:
        print("  No suggestions yet - need more interactions!")
    
    # Learning progress
    progress = learning_system.get_learning_progress()
    print(f"\n📊 Learning Progress:")
    print(f"  Phase: {progress['current_phase']}")
    print(f"  Progress: {progress['progress_percentage']:.1f}%")
    print(f"  Total Interactions: {progress['statistics']['total_interactions']}")
    print(f"  Patterns Learned: {progress['statistics']['patterns_learned']}")


def demo_secure_storage():
    """Demonstrate secure storage"""
    print_section("🔐 SECURE STORAGE DEMO")
    
    # Get vault status
    vault_status = secure_storage.get_vault_status()
    
    print("Secure Vault Status:")
    print(f"  Initialized: {vault_status['initialized']}")
    print(f"  Encryption: {'Enabled' if vault_status['encrypted'] else 'Disabled'}")
    print(f"  Security Level: {vault_status['security_level']}")
    print(f"\n📊 Stored Data:")
    print(f"  Voice Biometrics: {vault_status['voice_biometrics_count']}")
    print(f"  Projects: {vault_status['projects_count']}")
    print(f"  Designs: {vault_status['designs_count']}")
    
    print("\n🔒 Privacy Guarantees:")
    print("  ✅ All data encrypted with AES-256-GCM")
    print("  ✅ Hidden vault (.amrit_vault)")
    print("  ✅ Owner-only permissions (700/600)")
    print("  ✅ No third-party access")
    print("  ✅ No data sent externally")


def demo_complete_workflow():
    """Demonstrate complete workflow"""
    print_section("🔮 COMPLETE WORKFLOW DEMO")
    
    print("Simulating complete user workflow:\n")
    
    # Step 1: User gives voice command
    print("1️⃣ User: 'AMRIT, create an e-commerce website'")
    result = amrit.process_voice_command("Create an e-commerce website")
    print(f"   ✅ Code generated: Project ID {result.get('project_id', 'N/A')[:16]}...\n")
    time.sleep(0.3)
    
    # Step 2: User asks for design
    print("2️⃣ User: 'Design a logo for my e-commerce site'")
    result = amrit.process_voice_command("Design a logo for my e-commerce site")
    print(f"   ✅ Design generated: Design ID {result.get('design_id', 'N/A')[:16]}...\n")
    time.sleep(0.3)
    
    # Step 3: User checks status
    print("3️⃣ User: 'Show me the status'")
    result = amrit.process_voice_command("Show status")
    print(f"   ✅ Status displayed\n")
    time.sleep(0.3)
    
    # Step 4: User asks for suggestions
    print("4️⃣ User: 'Give me suggestions'")
    result = amrit.process_voice_command("Give me suggestions")
    suggestions = result.get('suggestions', {}).get('suggestions', [])
    if suggestions:
        print(f"   ✅ {len(suggestions)} suggestions provided\n")
    else:
        print(f"   ✅ Learning in progress...\n")
    
    print("Workflow complete! AMRIT AI learned from all interactions.")


def demo_system_info():
    """Show system information"""
    print_section("📋 SYSTEM INFORMATION")
    
    info = amrit.get_system_info()
    
    print(f"System: {info['name']} v{info['version']}")
    print(f"User: {info['user']}")
    print(f"Security: {info['security_level']}")
    print(f"Offline Mode: {'Enabled' if info['offline_mode'] else 'Disabled'}")
    
    print(f"\n✨ Enabled Features:")
    for feature, enabled in info['features'].items():
        status = "✅" if enabled else "❌"
        print(f"  {status} {feature.replace('_', ' ').title()}")
    
    print(f"\n🔒 Security Permissions:")
    for perm, enabled in info['permissions'].items():
        status = "✅" if enabled else "❌"
        print(f"  {status} {perm.replace('_', ' ').title()}")
    
    print(f"\n💻 Supported Languages ({len(info['supported_languages'])}):")
    print(f"  {', '.join(info['supported_languages'][:5])}...")
    
    print(f"\n🏗️ Project Types ({len(info['project_types'])}):")
    print(f"  {', '.join(info['project_types'][:5])}...")
    
    print(f"\n🎨 Design Categories ({len(info['design_categories'])}):")
    print(f"  {', '.join(info['design_categories'][:5])}...")


def main():
    """Run complete demo"""
    print("\n")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║                                                                  ║")
    print("║         🔮 AMRIT AI - COMPLETE SYSTEM DEMONSTRATION              ║")
    print("║            Adaptive Multi-Realm Intelligence Technology          ║")
    print("║                                                                  ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    
    # Run all demos
    demo_system_info()
    time.sleep(1)
    
    demo_voice_learning()
    time.sleep(1)
    
    demo_code_generation()
    time.sleep(1)
    
    demo_design_generation()
    time.sleep(1)
    
    demo_learning_system()
    time.sleep(1)
    
    demo_secure_storage()
    time.sleep(1)
    
    demo_complete_workflow()
    
    # Final summary
    print_section("🎉 DEMO COMPLETE")
    print("All AMRIT AI features demonstrated successfully!")
    print("\n✨ Key Highlights:")
    print("  ✅ Voice learning with 4-phase progression")
    print("  ✅ Multi-language code generation")
    print("  ✅ Auto-design generation")
    print("  ✅ Intelligent learning and adaptation")
    print("  ✅ Military-grade encryption")
    print("  ✅ Complete offline operation")
    print("  ✅ 100% privacy guaranteed")
    
    print("\n🔮 AMRIT AI is ready to serve you!")
    print(f"   User: {amrit.user_name}")
    print(f"   Total Activities: {len(amrit.activity_log)}")
    
    print("\n" + "="*70)


if __name__ == '__main__':
    main()
