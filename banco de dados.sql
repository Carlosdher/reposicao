CREATE DATABASE Projeto;

CREATE TABLE Usuario (
                matricula INTEGER NOT NULL;
                nome VARCHAR (255) NOT NULL;
                senha INTEGER NOT NULL;
                tipo SERIAL;
               PRIMARY KEY (matricula)
);

CREATE TABLE Planejamento (
                data_aula DATE NOT NULL,
                id_turma INTEGER NOT NULL,
                data_reposicao DATE NOT NULL,
                periodo VARCHAR (255) NOT NULL,
                descricao TEXT NOT NULL,
                id_planejamento SERIAL,
                PRIMARY KEY (id_planejamento)
	              FOREIGN KEY (data_reposicao) REFERENCES Solicitacao (data_da_reposicao),
                FOREIGN KEY (id_turma) REFERENCES Turma (id_turma),
                FOREIGN KEY (data_aula) REFERENCES Solicitacao (data_aula)
    );

CREATE TABLE Solicitacao (
                 data_da_reposicao TIMESTAMP NOT NULL,
                 data_aula DATE NOT NULL,
                 matricula INTEGER  NOT NULL,
                 data_falta_inicio TIMESTAMP NOT NULL,
                 data_falta_fim TIMESTAMP NOT NULL,
                 outro VARCHAR (255),
                 id_motivo INTEGER NOT NULL,
                 justificativa TEXT NOT NULL,
                 id_solicitacao SERIAL,
                 PRIMARY KEY (id_solicitacao),
                 FOREIGN KEY (matricula) REFERENCES Usuario (matricula),
                 FOREIGN KEY (id_motivo) REFERENCES Motivo (id_motivo),
                 UNIQUE(data_da_reposicao),
                 UNIQUE(data_aula)
);

CREATE TABLE Turma(
                id_turma SERIAL,
                nome varchar (255) NOT NULL,
                id_periodo INTEGER,
                PRIMARY KEY (id_turma),
                FOREIGN KEY (id_periodo) REFERENCES Periodo (id_periodo)
);

CREATE TABLE Motivo (
                id_motivo SERIAL,
                descricao TEXT NOT NULL,
                PRIMARY KEY (id_motivo)
);

CREATE TABLE Periodo (
              id_periodo SERIAL,
              nome VARCHAR (255),
              PRIMARY KEY (id_periodo)
);
