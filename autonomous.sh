#!/bin/bash

# Autonomous AI Developer Command
# Based on Cursor Forum Guide: https://forum.cursor.com/t/guide-a-simpler-more-autonomous-ai-workflow-for-cursor-new-update/70688/22?page=2

echo "🤖 Autonomous AI Developer - Japanese Kanji Project"
echo "=================================================="

# Check if we're in the right directory
if [ ! -f "cursorkleosr/project-config.md" ]; then
    echo "❌ Error: Not in Japanese Kanji project directory"
    echo "Please run this command from the project root directory"
    exit 1
fi

# Check if todo.md exists
if [ ! -f "todo.md" ]; then
    echo "❌ Error: todo.md not found"
    echo "Please ensure todo.md exists in the project root"
    exit 1
fi

echo "✅ Project structure verified"
echo ""

# Display current state
echo "📊 Current State:"
echo "----------------"
if [ -f "cursorkleosr/workflow_state.md" ]; then
    grep -A 5 "## State" cursorkleosr/workflow_state.md | head -6
else
    echo "⚠️  workflow_state.md not found"
fi

echo ""
echo "📋 Next Tasks:"
echo "-------------"
if [ -f "todo.md" ]; then
    grep -A 10 "^- \[ \]" todo.md | head -10
else
    echo "⚠️  todo.md not found"
fi

echo ""
echo "🎯 Autonomous Workflow Protocol:"
echo "1. Read project_config.md (LTM) and workflow_state.md (STM)"
echo "2. Consult Rules based on current State"
echo "3. Act via Cursor tools"
echo "4. Update workflow_state.md immediately after actions"
echo "5. Work on next unchecked task in todo.md"
echo ""

echo "🚀 Ready for autonomous execution!"
echo "Use Cursor AI with the prompt:"
echo ""
echo "You are an autonomous AI developer using a two-file system. Your sole sources of truth are @project_config.md (LTM) and @workflow_state.md (STM/Rules/Log). Before every action, read workflow_state.md, consult ## Rules based on ## State, act via Cursor, then immediately update workflow_state.md. Look at @todo.md and work on the next unchecked task."
