pipeline {
    agent any

    environment {
        python_version = "3"
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/adhavswapna/hello-world-flask.git']])
                }
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    // Install dependencies                
                    sh 'pip install Flask nose'
                    
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run unit test using nose
                    sh python-3
                    sh 'nosetests hello-world-flask'
                }
            }
        }
    }

    post {
        success {
            echo 'Unit tests passed! Build is successful.'
        }
        failure {
            echo 'Unit tests failed. Build is unsuccessful.'
        }
    }
}
