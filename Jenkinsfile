pipeline{
    agent any 
    stages {
		
  
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
		sh 'pwd'
            }
            
        }
        stage("test") {
            steps {
                echo 'testing stage is running'
		sh 'python3 test_farecalculationsystem.py'
		//sh 'pylint farecalculationsystem.py'
		
		
            }
        }
        stage("deploy") {
            steps {
                echo 'deploy stage is running'
		sh "sudo scp -i 'key-v-pooja.pem' -o StrictHostKeyChecking=no -r * ubuntu@ec2-54-242-218-60.compute-1.amazonaws.com:/tmp"
		sh "sudo ssh -i 'key-v-pooja.pem' ubuntu@ec2-54-242-218-60.compute-1.amazonaws.com"
		sh 'cd /tmp'
		sh 'ls'
		//sh 'sudo scp -i /home/ubuntu/key-value-pair-20879.pem -o StrictHostKeyChecking=no -r /var/lib/jenkins/workspace/Pipeline/  ec2-18-234-167-65.compute-1.amazonaws.com:/tmp'
            }
        }
    }
    post {
        failure {
            echo 'building is failed'
        }
	always {
	    echo "pipeline finished successfully"	
	}
    }
}
