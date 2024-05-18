pipeline {
agent { dockerfile true }
   stages {
        stage('Runsh') {
            steps {
               sh 'pwd'
                sh  'bash hello_there.sh'
                sh  'python tests/tests.py'
            }
        }
    }
}
