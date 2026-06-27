pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "hanane2277/scsj4383-app"
        GITHUB_REPO = "https://github.com/hanane2277/SCSJ4383-DevOps-Project.git"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning GitHub repository...'
                git branch: 'main', url: "${GITHUB_REPO}"
                echo 'Code checked out successfully!'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                bat 'pip install -r requirements.txt --quiet'
                echo 'Build completed!'
            }
        }

        stage('Test') {
            steps {
                echo 'Running application tests...'
                bat '''
                    pip install pytest --quiet
                    python -m pytest test_app.py -v
                '''
                echo 'Tests passed!'
            }
        }

        stage('Performance Test - JMeter') {
            steps {
                echo 'Running JMeter performance tests...'
                bat '''
                    if exist "C:\\apache-jmeter\\bin\\jmeter.bat" (
                        C:\\apache-jmeter\\bin\\jmeter.bat -n -t jmeter_test.jmx -l jmeter_results.jtl
                        echo JMeter tests completed
                    ) else (
                        echo JMeter not installed - skipping performance test
                        echo Performance test stage demonstrated
                    )
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                bat "docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} -t ${DOCKER_IMAGE}:latest ."
                echo 'Docker image built successfully!'
            }
        }

        stage('Docker Push') {
            steps {
                echo 'Pushing Docker image to Docker Hub...'
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"
                    bat "docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}"
                    bat "docker push ${DOCKER_IMAGE}:latest"
                }
                echo 'Docker image pushed to Docker Hub!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully! All stages passed.'
        }
        failure {
            echo 'Pipeline failed! Check the logs above.'
        }
        always {
            echo "Build #${BUILD_NUMBER} finished."
        }
    }
}
