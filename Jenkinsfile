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
		sh 'apt-get install python-virtualenv'
		sh 'virtualenv -p /usr/bin/python3 virtualenvironment/myvenv'
		sh 'cd virtualenvironment/myvenv/bin'
		sh 'source activate'
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
