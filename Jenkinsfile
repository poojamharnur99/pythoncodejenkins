pipeline{
    agent { docker { image 'python:3.5.1' } } 
    stages {
        stage("build") {
            steps {
                echo 'build stage is running'
		sh 'python --version' 
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
