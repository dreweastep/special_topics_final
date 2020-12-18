//pipeline
pipeline {
  agent { docker { image 'python:latest' 
                   args '--user 0:0'}}
  stages {
   stage('build') {
    steps {
      sh 'pip3 install --no-cache-dir -r requirements.txt' 
   }
  }
  stage('test') {
   steps {
     sh 'python3 test.py'
    } 
   }
  }
}
