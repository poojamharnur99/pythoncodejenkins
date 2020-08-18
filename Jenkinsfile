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
		sh 'ssh -i "key-value-pair-20879.pem" ubuntu@ec2-34-207-55-251.compute-1.amazonaws.com'
		//sh 'python test_farecalculationsystem.py' 
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
