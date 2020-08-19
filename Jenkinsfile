pipeline{
    agent any 
    stages {
		
  	//stage to checkout scm
	stage("Checkout") { 
      	    steps {
                checkout scm
     	    }
	}
	 //build stage to create virtual environment 
        stage("build") {
            steps {
	
                echo 'build stage is running'
		sh 'ls' 
		
		sh 'PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH'
		//create virtual environment
		sh 'virtualenv venv'
		sh 'cd venv/bin/'
		sh 'pwd'
            }
            
        }
	 //test stage to testing python application
        stage("test") {
            steps {
                echo 'testing stage is running'
		//unit testinf for python application
		sh 'python3 test_farecalculationsystem.py'
		sh 'pylint farecalculationsystem.py'
		
		
            }
        }
	 //deploy our application from jenkins server to other ec2 instance
        stage("deploy") {
            steps {
                echo 'deploy stage is running'
		//copy files from jenkins server to other ec2 instance
		sh "sudo scp -i 'key-pair-jenkins-pooja.pem' -o StrictHostKeyChecking=no -r * ubuntu@ec2-52-86-124-197.compute-1.amazonaws.com:/tmp"
		//connect to ec2 instance from jenkins server
		sh "sudo ssh -i 'key-pair-jenkins-pooja.pem' ubuntu@ec2-52-86-124-197.compute-1.amazonaws.com"
		sh 'cd /tmp'
		sh 'ls'
		//create virtual environment into that instance from jenkins server
		sh 'cd venv/bin/'
		run python application
		sh 'python3 test_farecalculationsystem.py'
		
            }
        }
    }
    post {
        failure {
            echo 'pipline building is failed at some point'
        }
	always {
	    echo "pipeline finished "	
	}
    }
}
