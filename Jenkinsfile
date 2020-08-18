pipeline{
    agent any
    stages {
        stage("build") {
            steps {
                echo 'build stage is running'
		sh 'python --version'		
                sh 'chmod +x test_farecalculationsystem.py'
                sh './test_farecalculationsystem.py' 
            }
            
        }
        stage("test") {
            steps {
                echo 'testing stage is running'
            }
        }
        stage("deploy") {
            steps {
                echo 'deploy stage is running'
            }
        }
    }
    post {
        failure {
            echo 'building is failed'
        }
    }
}
