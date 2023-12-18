pipeline {
    agent any

    environment {
        python_version ="3"
    }

    stages {
        stage('Checkout') {
            steps {
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
                sh 'pip install -r requirements.txt'
            }
        }
    }
    
    stage('Run Tests') {
        steps {
            script{
                //Run unit test using nose
                sh "nosetests unit_test/"
                }
            }
        }

    post {
        success {
            echo 'Unit tests passed! Build is successful.'
            }
        failure {
            echo 'Unit tests failed Build is unsuccessful.'
            }
        }
    
