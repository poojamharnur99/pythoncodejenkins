pipeline{
    agent any 
    stages {
	stage("Cleanupworkspace") { 
      	    steps {
            	cleanWs()
     	    }
	}	
  
	stage("Checkout") { 
      	    steps {
                checkout scm
     	    }
	}	
        stage("build") {
            steps {
	
                echo 'build stage is running'
		sh 'ls' 
		
		sh 'PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH'
		sh 'virtualenv venv'
		sh 'cd venv/bin/'
		sh 'apt-get update'
		sh 'apt-get install pylint'
            }
            
        }
        stage("test") {
            steps {
                echo 'testing stage is running'
		sh 'python3 test_farecalculationsystem.py'
		
		
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
