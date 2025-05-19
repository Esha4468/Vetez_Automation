# Vetez_Automation_Installation_Process

**#_Prerequisites**
| Tool                        | Purpose                         | Required?      | Download                                                                                  |
| --------------------------- | ------------------------------- | -------------- | ----------------------------------------------------------------------------------------- |
| **Python (3.7+)**           | Write test scripts              | ✅              | [python.org](https://www.python.org/downloads/)                                           |
| **Java JDK (8 or 11+)**     | Required for Android automation | ✅              | [Oracle JDK](https://www.oracle.com/java/technologies/javase-downloads.html)              |
| **Node.js + npm**           | Required to install Appium      | ✅              | [nodejs.org](https://nodejs.org)                                                          |
| **Android Studio**          | Android SDK, Emulator           | ✅              | [developer.android.com/studio](https://developer.android.com/studio)                      |
| **Appium CLI**              | Automation server               | ✅              | Installed via npm                                                                         |
| **Appium Python Client**    | Python bindings for Appium      | ✅              | Installed via pip                                                                         |
| **Appium Inspector**        | Inspect app UI & get locators   | 🟡 Recommended | [Inspector releases](https://github.com/appium/appium-inspector/releases)                 |
| **IDE (VS Code / PyCharm)** | Write your code                 | ✅              | [VS Code](https://code.visualstudio.com/) / [PyCharm](https://www.jetbrains.com/pycharm/) |

**Envirnment Set Up**
1. Install Python & pip (Check Installation on cmd
    [ python --version
      pip --version     ]

2. Install Java JDK ans set Environment(check on cmd---> java -version)
3. Install Node.js + npm ( check on cmd-----> node -v  and
npm -v)
4. Install Android Studio( SDK Tools, SDK Platforms, Android Emolator)  (For check connected device run -----> adb devices) for device connection check the following steps:
    ✅ Step 1: Download Android Studio
    ✅ Step 2: Install Required SDK Components When the Android Studio Setup Wizard runs:Check all options including:
          ✅ Android SDK
          ✅ Android SDK Platform Tools
          ✅ Android Emulator
          ✅ Android Virtual Device
       After installation---> Open Android Studio--->Go to--->Tools → SDK Manager
        **  Make sure these are installed:**
            -Android SDK Tools
            -Android SDK Platform-tools
            -Android SDK Build-tools
            -SDK Platforms (like Android API 30, 31, etc.)
   ✅ Tip: Install the latest Stable version of an SDK platform (e.g., API 35).

   ✅ Step 3: Create a Virtual Device (Emulator)
         -Go to Tools → Device Manager-->Click Create Device-->Choose a device model (e.g., Pixel 4 or Nexus 5)--->Choose a system image (e.g., Android 11 - API 30)-->Click Next → Finish

   ✅ Step 4: Set Environment Variables ** (Important!)** This step allows your system and tools like adb or Appium to recognize the Android SDK.
   --On Windows--
     1. Set ANDROID_HOME: Environment Variables--->Under User Variables or System Variables, click New-----> Variable name: ANDROID_HOME-->Variable value (default install path of sdk folder) like --> C:\Users\YourUser\AppData\Local\Android\Sdk  {Replace YourUser with 
      your actual Windows username.}

     2. Add to PATH
       In the Path variable (Edit----> New), add these lines:
                 %ANDROID_HOME%\platform-tools
                 %ANDROID_HOME%\emulator
                 %ANDROID_HOME%\tools
                 %ANDROID_HOME%\tools\bin
         Now Click OK → OK → Apply.
     ✅ Step 5: Verify Installation: Run-----> adb devices  ----> If everything is correct, you’ll see something like:
           **List of devices attached
              abd5645554   device **
5. Install Appium CLI  (Run this on cmd ----> npm install -g appium  , after run this for check  run----->  appium -v . To start Appium server run -------> appium )Install Appium CLI  (Run this on cmd ----> npm install -g appium  , after run this for check  run----->  appium -v . To start Appium server run -------> appium )
6. Install Appium Python Client---> Run----> pip install Appium-Python-Client selenium
7.  Install and Use Appium Inspector Download from: https://github.com/appium/appium-inspector/releases

 





   

