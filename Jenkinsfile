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

                scripts {
                    Checkout git 'https://github.com/adhavswapna/hello-world-flask.git'
                
                }
            
            }
        }
    }
}
    
    stage('Install dependenies'){
        steps {
            script {
                //install dependencies
                sh 'pip install Flask pytest'
            }
        }
    }
    
    stage('Run Tests') {
        steps {
            script{            
                sh 'python -m unittest/unit_test.py'
                
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

