pipeline {
    agent any
    parameters {
        choice(name: 'TEST_SUITE', choices: ['Smoke', 'Smoke&Regression'], description: 'Набор тестов')
        string(name: 'TEST_BRANCH_NAME', defaultValue: 'main', description: 'Ветка для запуска автотестов')
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '${TEST_BRANCH_NAME}']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/and-yatsenko/python_AQA_learning.git']])
            }
        }
        stage('Build') {
            steps {
                 // Создание виртуальной среды и установка пакетов
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                // Запуск автотестов
                script {
                    if (params.TEST_SUITE == 'Smoke') {
                        sh '. venv/bin/activate && pytest -s -v -m smoke --alluredir allure-results'
                    } else if (params.TEST_SUITE == 'Smoke&Regression') {
                        sh '. venv/bin/activate && pytest -s -v -m "smoke and regression" --alluredir allure-results'
                    }
                }
            }
        }
        stage('Reports') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}