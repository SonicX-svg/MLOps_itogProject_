pipeline {
agent { dockerfile true }
   stages {
        stage('Runsh') {
            steps {
               sh 'hello'
                sh  'bash hello_there.sh'
                sh  'python tests/tests.py'
            }
        }
    }
}
