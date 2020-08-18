pipeline{
    agent any
    stages {
        stage("build") {
            steps {
                echo 'build stage is running'
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
