pipeline {
agent { dockerfile true }
   stages {
        stage('Runsh') {
            steps {
               sh 'echo hello'
                sh  'bash hello_there.sh'
            }}
         stage('Run flake8 linter') {
           steps {
               sh '''
                   flake8 model_creation.py
                   flake8 model_preprocessing.py
                   flake8 test_model.py
                   flake8 tests/tests.py
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

