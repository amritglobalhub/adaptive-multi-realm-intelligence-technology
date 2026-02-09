# 🚀 AMRIT AI - Quick Start Guide

Get started with AMRIT AI in 5 minutes!

---

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `cryptography` - For military-grade encryption
- `flask` - For offline web server capabilities
- `flask-cors` - For API server functionality

---

## Step 2: Run Your First Command

### Interactive Mode (Recommended)

```bash
python amrit_cli.py
```

Then try these commands:
```
> Create a Python website
> Design a logo
> Show status
> Help
```

### Single Command Mode

```bash
python amrit_cli.py --command "Create a Python website"
```

---

## Step 3: Check System Status

```bash
python amrit_cli.py --status
```

You'll see:
- 🎤 Voice Learning progress
- 🧠 Learning System statistics
- 🔐 Secure Vault contents
- 📊 Overall system health

---

## Step 4: Run the Demo

```bash
python demo.py
```

This demonstrates:
- Voice learning system
- Code generation (Python, JavaScript, Java, C++)
- Design generation (Logo, UI/UX, Brand Identity)
- Learning and adaptation
- Secure encrypted storage
- Complete workflow

---

## Example Commands

### Code Generation

```
"Create a Python website"
"Build an e-commerce app"
"Generate REST API in JavaScript"
"Make a mobile app in Java"
"Create a CLI tool in Python"
```

### Design Generation

```
"Create a logo"
"Design a UI/UX"
"Generate brand identity"
"Make a color scheme"
"Design a modern layout"
```

### System Commands

```
"Show status"
"What's my progress?"
"Give me suggestions"
"Help"
```

---

## Understanding the Learning Phases

### Phase 1: Recognition (1-7 days)
- **Goal**: Learn your voice patterns
- **Samples Needed**: 100
- **Status**: Basic voice recognition

### Phase 2: Learning (1-4 weeks)
- **Goal**: Understand your preferences
- **Samples Needed**: 500
- **Status**: Preference capture

### Phase 3: Adaptation (1-3 months)
- **Goal**: Adapt to your needs
- **Samples Needed**: 2,000
- **Status**: Intelligent anticipation

### Phase 4: Mastery (3+ months)
- **Goal**: Perfect understanding
- **Samples Needed**: 5,000+
- **Status**: Complete autonomy

---

## Using Python API Directly

```python
from amrit_ai import amrit

# Process voice command
result = amrit.process_voice_command('Create a Python website')
print(result)

# Generate code
from code_generator import code_generator
code = code_generator.generate_code(
    description="E-commerce platform",
    language="Python",
    project_type="Website"
)

# Generate design
from design_generator import design_generator
design = design_generator.generate_design(
    design_type="Logo",
    description="Tech startup logo"
)

# Get suggestions
from learning_system import learning_system
suggestions = learning_system.make_suggestion()
print(suggestions)
```

---

## Security & Privacy

### What's Protected?
✅ All data encrypted with AES-256-GCM  
✅ Hidden vault (`.amrit_vault/`)  
✅ Owner-only permissions (700/600)  
✅ No external data transmission  
✅ Complete offline operation  

### Where is Data Stored?
```
.amrit_vault/
├── .encryption_key       # Encrypted key
├── voice_biometrics/     # Voice patterns
├── preferences/          # User preferences
├── generated_projects/   # Code projects
├── generated_designs/    # Design assets
└── learned_patterns/     # Learning data
```

---

## Troubleshooting

### "Module not found"
```bash
pip install -r requirements.txt
```

### "Permission denied"
```bash
chmod +x amrit_cli.py demo.py
```

### Start Fresh
```bash
rm -rf .amrit_vault/
python amrit_cli.py
```
This will reinitialize with a new encryption key.

---

## What's Next?

1. **Use regularly** - The more you use it, the better it learns
2. **Provide feedback** - Help AMRIT improve
3. **Explore features** - Try code generation, design, suggestions
4. **Check progress** - Monitor learning phases
5. **Stay secure** - Your data never leaves your machine

---

## Quick Reference

| Command | Description |
|---------|-------------|
| `python amrit_cli.py` | Interactive mode |
| `python amrit_cli.py --command "..."` | Single command |
| `python amrit_cli.py --status` | System status |
| `python demo.py` | Run demo |
| `python amrit_ai.py` | Direct Python execution |

---

## Support

For detailed documentation, see [AMRIT_AI_DOCUMENTATION.md](AMRIT_AI_DOCUMENTATION.md)

For help within the system:
```bash
python amrit_cli.py --command "help"
```

---

**🔮 You're ready to use AMRIT AI!**

*Start with simple commands and let AMRIT learn from your interactions.*
