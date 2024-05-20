pipeline {
agent { dockerfile true }
   stages {
        stage('Runsh') {
            steps {
               sh 'echo hello'
                sh  'bash hello_there.sh'
            }
            stage('Run formater') {
              steps {
                  sh '''
                      black model_creation.py
                      black model_preprocessing.py
                      black test_model.py
                      balck tests/tests.py
                  '''
              }}
            stage('Run tests') {
                 steps {
                     sh '''
                      sh  'python tests/tests.py'
                     '''
                 }      
            }
        }
    }
}
