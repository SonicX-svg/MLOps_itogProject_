pipeline {
agent { dockerfile true }
   stages {
        stage('Runsh') {
            steps {
               sh 'pwd'
                sh  'bash hello_there.sh'
            }
        }
        stage('Run_tests') {
            steps {
                sh  'python tests/tests.py'
            }
        }      
    }
}
