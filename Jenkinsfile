pipeline {
agent { dockerfile true }
   stages {
        stage('Runsh') {
            steps {
               sh 'pwd'
                sh  'go.sh'
            }
        }
        stage('Run_tests') {
            steps {
                sh  'echo start tests'
                sh  'python tests/tests.py'
            }
        }      
    }
}
