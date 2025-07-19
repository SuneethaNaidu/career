import random
import json

# Expanded skills pool
sample_skills = [
    "html", "css", "javascript", "react", "nodejs", "express", "typescript", "nextjs",
    "python", "flask", "django", "java", "spring", "kotlin", "c", "c++", "c#", "r",
    "swift", "flutter", "dart", "sql", "mongodb", "postgresql", "firebase", "aws",
    "azure", "gcp", "docker", "kubernetes", "linux", "git", "github", "bash",
    "machine learning", "deep learning", "nlp", "opencv", "pandas", "numpy", "matplotlib",
    "data structures", "algorithms", "oop", "design patterns", "microservices", "rest api",
    "graphql", "figma", "adobe xd", "ui design", "ux research", "seo", "content writing",
    "cybersecurity", "networking", "maths", "physics", "calculus", "linear algebra", 
    "statistics", "problem solving", "communication", "teamwork", "public speaking",
    "project management", "agile", "scrum"
]

# Expanded project ideas
sample_projects = [
    "Portfolio Website", "ToDo App", "Weather App", "Blog Platform", "Chat App",
    "Note Keeper", "Stock Price Tracker", "Task Scheduler", "Data Visualizer",
    "Image Classifier", "Object Detector", "E-commerce Store", "Login System",
    "AI Chatbot", "Fitness Tracker", "Expense Manager", "Quiz App", "News Aggregator",
    "PDF to Text Converter", "Video Streaming Platform", "Video Editing Tool",
    "Online Code Editor", "Speech-to-Text App", "Face Recognition Attendance",
    "Crypto Dashboard", "Flight Price Predictor", "Resume Builder", 
    "Online Judge System", "Social Media Dashboard", "Movie Recommender System",
    "Banking System in Java", "Compiler in C", "Physics Simulation",
    "Math Solver", "Virtual Classroom", "Online Survey System",
    "Real-time Chat + Video App", "3D Model Viewer", "Portfolio with Blog + CMS",
    "Personal Finance Manager", "Voice-controlled App", "IoT Device Controller",
    "Multi-language Translator", "Currency Converter", "Portfolio using Three.js",
    "Stock Market Alert Bot", "Typing Speed Game", "Virtual Lab Simulation",
    "YouTube Audio Downloader", "Instagram Clone", "Job Recommendation System"
]

# Expanded resources
sample_resources = [
    "https://www.freecodecamp.org/learn",
    "https://developer.mozilla.org/en-US/",
    "https://reactjs.org/docs/getting-started.html",
    "https://nodejs.org/en/learn",
    "https://expressjs.com/",
    "https://docs.python.org/3/",
    "https://realpython.com/",
    "https://flask.palletsprojects.com/",
    "https://spring.io/guides",
    "https://www.w3schools.com/",
    "https://www.geeksforgeeks.org/",
    "https://www.udemy.com",
    "https://www.coursera.org",
    "https://www.kaggle.com/learn",
    "https://www.datacamp.com/",
    "https://brilliant.org/",
    "https://ocw.mit.edu/",
    "https://www.edx.org/",
    "https://machinelearningmastery.com/",
    "https://docs.docker.com/",
    "https://kubernetes.io/docs/home/",
    "https://www.codecademy.com/",
    "https://www.hackerrank.com/",
    "https://www.leetcode.com/",
    "https://github.com/explore",
    "https://firebase.google.com/docs",
    "https://cloud.google.com/docs",
    "https://aws.amazon.com/training/",
    "https://learn.microsoft.com/en-us/training/",
    "https://roadmap.sh/",
    "https://cs50.harvard.edu/x/",
    "https://docs.opencv.org/",
    "https://pytorch.org/tutorials/",
    "https://keras.io/examples/",
    "https://docs.github.com/",
    "https://www.youtube.com/@Fireship",
    "https://www.youtube.com/@TechWithTim",
    "https://www.youtube.com/@TheCodingTrain",
    "https://developer.android.com/training",
    "https://developer.apple.com/"
]

# Custom handpicked entries
custom_paths = {
    "Python Developer": {
        "skills": ["python", "flask", "sql", "git"],
        "projects": ["Web Scraper", "REST API"],
        "resources": ["https://realpython.com", "https://docs.python.org/3/"]
    },
    "Java Developer": {
        "skills": ["java", "spring", "oop", "sql"],
        "projects": ["Banking System", "Library Manager"],
        "resources": ["https://www.geeksforgeeks.org/", "https://www.udemy.com"]
    },
    "C Programmer": {
        "skills": ["c", "data structures", "algorithms"],
        "projects": ["Compiler Design", "File System Emulator"],
        "resources": ["https://ocw.mit.edu/", "https://www.w3schools.com/"]
    },
    "Mathematician": {
        "skills": ["maths", "calculus", "linear algebra", "statistics"],
        "projects": ["Equation Solver", "Data Analyzer"],
        "resources": ["https://brilliant.org/", "https://ocw.mit.edu/"]
    },
    "Physicist": {
        "skills": ["physics", "maths", "simulation", "problem solving"],
        "projects": ["Projectile Motion Simulator", "Circuit Simulator"],
        "resources": ["https://ocw.mit.edu/", "https://brilliant.org/"]
    }
}

# Generate a random career entry
def generate_random_career(index):
    title = f"Career Path {index}"
    return {
        title: {
            "skills": random.sample(sample_skills, random.randint(4, 7)),
            "projects": random.sample(sample_projects, random.randint(3, 4)),
            "resources": random.sample(sample_resources, random.randint(3, 5))
        }
    }

# Build final dataset
career_data = custom_paths.copy()

for i in range(6, 201):
    career_data.update(generate_random_career(i))

# Save as JSON
with open("career_data.json", "w") as f:
    json.dump(career_data, f, indent=4)

# Optional: Print preview of first 5
print("Preview of Career Data:")
for k in list(career_data.keys())[:5]:
    print(f"{k}: {career_data[k]}")
