pipeline {
    agent any

    stages {

        stage('Code Linting') {
            steps {
                echo 'Linting Stage'
            }
        }

        stage('Code Build') {
            steps {
                echo 'Building Docker Image'
                sh 'docker build -t devops-app .'
            }
        }

        stage('Containerized Deployment') {
            steps {
                echo 'Deploying Container'

                sh 'docker stop devops-container || true'
                sh 'docker rm devops-container || true'

                sh 'docker run -d --name devops-container -p 5000:5000 devops-app'
            }
        }

        stage('Containerized Selenium Testing') {
            steps {
                echo 'Running Selenium Tests'

                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                python test_app.py
                '''
            }
        }
    }
}
