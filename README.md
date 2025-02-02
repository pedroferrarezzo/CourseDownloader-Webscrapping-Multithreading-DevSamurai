# DEV SAMURAI COURSE DOWNLOADER
https://class.devsamurai.com.br

## Description
This repository contains a Python script that allows you to download all the courses made available by the Dev Samurai platform, following the announcement of its closure. The script uses multithreading to perform simultaneous downloads, making the process of obtaining the content faster and easier.<br>
The goal is to highlight the platform's generosity, which made all its courses available for download, ensuring lifetime access to the material.

## Platform Notice - IMPORTANT
Dear students,

With great gratitude and respect, we are reaching out to share an important update about our journey at Dev Samurai.

After years dedicated to teaching programming and helping thousands of students develop skills and achieve their professional goals, we have made the decision to close the services of our teaching platform. This decision was made with great care and consideration for all of you, who are the reason we've come this far.

We understand that continued access to knowledge is essential for everyone’s success. Therefore, we have made all the content from our courses available for download right below on this site, with a total size of approximately 100GB (which can be stored on a simple 128GB USB drive). This ensures you have lifetime access to all the material and can continue learning at your own pace.

**IMPORTANT:** The files will be available for download until December 2025. Don’t wait until the last minute!

To make it easier, we encourage everyone interested to download the courses as soon as possible. If you have any questions or difficulties, our team is here to assist. You can reach us by email at suporte@devsamurai.com.br.

We sincerely thank you for your trust in Dev Samurai throughout this journey. The learning and success of each of you have always motivated us to continue creating high-quality content.

We wish you all much success and growth in your careers and projects. May this farewell be just a new beginning on the learning path.

With gratitude,
Dev Samurai Team

## Course List
- Live Classes
- Backend - Mastering NodeJS
- Backend - Mastering Postgres
- Programmer Career
- Flutter - IMC Calculator
- Flutter - Online Menu
- Flutter - Fluck Noris
- Flutter - Reading List
- Advanced Flutter
- Basic Flutter
- Flutter Snippets
- Frontend - Bootstrap
- Frontend - CSS Grid
- Frontend - Creating Your Resume
- Frontend - Creating Your Portfolio
- Frontend - HTML Resume
- Frontend - Understanding HTML with CSS
- Frontend - Flexbox
- Frontend - Registration Form
- Frontend - Basic HTML
- Frontend - Coffee Shop
- Frontend - Mobile First
- Frontend - Preprocessors (Sass)
- Frontend - Your First Web Page
- Full Stack - Food Commerce
- Ionic
- JavaScript - Password Generator
- JavaScript - Basic to Advanced
- Kapi Academy - API Supreme
- Linux for Programmers
- Advanced Programming Logic
- Basic Programming Logic
- Master Classes
- My First Opportunity
- Minicourse Program from Scratch
- Open Mentoring
- Setting up the Dev Environment
- First Opportunity
- Program from Scratch - HTML
- Program from Scratch - Rock Paper Scissors
- Program from Scratch - Ping-Pong
- Program from Scratch
- Python - Hangman
- Python - Guessing Game
- Python - Snake Game
- Python - Compound Interest
- Python - Fipe Table
- Advanced Python
- Basic Python
- React - Github API
- React - Fundamentals
- React - Reading List
- React Native - IMC Calculator
- React Native - Publishing the App
- React Native - Smart Money - Firebase
- React Native - Smart Money - Navigation V5
- React Native - SmartMoney - Login
- React Native - SmartMoney
- React Native - TODO
- React Native
- Extra Income 10x - Interviews
- Extra Income 10x - Unshakable Mindset
- Extra Income 10x - System Pricing
- Extra Income 10x - Extra Training
- Extra Income 10x
- TypeScript - TODO List
- Basic TypeScript

## HOW TO USE

1. Clone this repository:
   ```sh
    git clone https://github.com/your-username/dev-samurai-course-downloader.git
   
2. Initialize a Venv and install dependencies:
   ```sh
    # Create the Venv
    python -m venv venv
   
    # Activate the Venv - Windows
    .\venv\Scripts\activate

    # Activate the Venv - Linux/macOS:
    source venv/bin/activate

    # Install BS4
    pip install requests beautifulsoup4

3. Modify the variable for the download directory:
    ```sh
    # NOTE: the content is approximately 100GB. Ensure you have available space on your disk/USB drive.
    ...
    if __name__ == '__main__':
      url = 'https://class.devsamurai.com.br'
      download_folder = r'C:\Users\User\Downloads' # Example
    ...
    
4. OPTIONAL: Increase the number of threads used for downloading:
    ```sh

    # NOTE: increasing the number of threads results in more simultaneous downloads. This can speed up the download process but will also increase bandwidth usage and load on the server. Use with caution to avoid overloading your connection or the platform.
    # Multiple simultaneous connections from the same client can also be interpreted as suspicious behavior, potentially leading to access restrictions or temporary bans. I recommend adjusting the number of threads with moderation to avoid connectivity issues.

    ...
    threads = []
    for _ in range(x):  # x -> Number of threads
        ...
        threads.append(thread)
    ...

5. Run the Project:
    ```sh
    python DownloadDevSamuraiCourses.py

6. The download will begin. Monitor the terminal output to see which course is being downloaded and if it completed successfully:
   ![image](https://github.com/user-attachments/assets/8e627c82-d9d5-4f4c-bbb9-7752eaf7aea9)
