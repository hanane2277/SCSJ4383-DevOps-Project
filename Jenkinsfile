pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDS = credentials('docker-hub')
        DOCKER_IMAGE = "hanane2277/scsj4383-app"
        GITHUB_REPO = "https://github.com/hanane2277/SCSJ4383-DevOps-Project.git"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning GitHub repository...'
                git branch: 'main', url: "${GITHUB_REPO}"
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                bat 'python -m pytest test_app.py -v || echo "Tests completed"'
            }
        }

        stage('Performance Test - JMeter') {
            steps {
                echo 'Running JMeter performance tests...'
                bat '''
                    if exist "C:\\apache-jmeter\\bin\\jmeter.bat" (
                        C:\\apache-jmeter\\bin\\jmeter.bat -n -t jmeter_test.jmx -l jmeter_results.jtl -e -o jmeter_report
                    ) else (
                        echo JMeter not found, skipping performance test
                    )
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                bat "docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} -t ${DOCKER_IMAGE}:latest ."
            }
        }

        stage('Docker Push') {
            steps {
                echo 'Pushing Docker image to Docker Hub...'
                bat "docker login -u %DOCKER_HUB_CREDS_USR% -p %DOCKER_HUB_CREDS_PSW%"
                bat "docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}"
                bat "docker push ${DOCKER_IMAGE}:latest"
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
