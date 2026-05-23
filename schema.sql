-- ════════════════════════════════════════════════════════════════════════════
-- CONSCIENCE PSICOLOGIA - DATABASE SCHEMA
-- ════════════════════════════════════════════════════════════════════════════

-- Tabela: pacientes
CREATE TABLE IF NOT EXISTS pacientes (
  id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  nome TEXT NOT NULL,
  email TEXT,
  telefone TEXT,
  data_nascimento DATE,
  cpf TEXT UNIQUE,
  endereco TEXT,
  cidade TEXT,
  estado TEXT,
  cep TEXT,
  observacoes TEXT,
  criado_em TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  atualizado_em TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Tabela: sessoes
CREATE TABLE IF NOT EXISTS sessoes (
  id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  paciente_id BIGINT NOT NULL REFERENCES pacientes(id) ON DELETE CASCADE,
  data_sessao DATE NOT NULL,
  hora_inicio TIME,
  duracao INTEGER, -- em minutos
  origem TEXT NOT NULL CHECK (origem IN ('particular', 'volare', 'amar-ter', 'amar-qua', 'amar-qui')),
  tipo TEXT CHECK (tipo IN ('individual', 'plano4')), -- para particular
  valor DECIMAL(10, 2),
  status_pagamento TEXT DEFAULT 'pendente' CHECK (status_pagamento IN ('pendente', 'pago', 'atraso', 'plano')),
  data_pagamento DATE,
  forma_pagamento TEXT,

  -- Para planos (Volare e Amar)
  convenio TEXT,
  duracao_plano INTEGER CHECK (duracao_plano IN (20, 40)),
  valor_unitario DECIMAL(10, 2),
  numero_guia TEXT,
  sessoes_realizadas INTEGER DEFAULT 0,
  sessoes_pagas INTEGER DEFAULT 0,

  -- NF
  nf_emitida BOOLEAN DEFAULT FALSE,
  data_emissao_nf DATE,
  numero_nf TEXT,

  observacoes TEXT,
  criada_em TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  atualizado_em TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Tabela: agendamentos
CREATE TABLE IF NOT EXISTS agendamentos (
  id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  paciente_id BIGINT NOT NULL REFERENCES pacientes(id) ON DELETE CASCADE,
  data DATE NOT NULL,
  hora TIME NOT NULL,
  origem TEXT NOT NULL CHECK (origem IN ('particular', 'volare', 'amar-ter', 'amar-qua', 'amar-qui')),
  tipo TEXT,
  valor DECIMAL(10, 2),
  convenio TEXT,
  duracao INTEGER,
  valor_unitario DECIMAL(10, 2),
  observacoes TEXT,
  confirmado BOOLEAN DEFAULT FALSE,
  sessao_id BIGINT REFERENCES sessoes(id) ON DELETE SET NULL,
  criado_em TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  atualizado_em TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Tabela: notas_fiscais
CREATE TABLE IF NOT EXISTS notas_fiscais (
  id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  sessao_id BIGINT NOT NULL REFERENCES sessoes(id) ON DELETE CASCADE,
  numero_nf TEXT UNIQUE,
  data_emissao DATE NOT NULL,
  criada_em TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Índices para performance
CREATE INDEX IF NOT EXISTS idx_sessoes_paciente ON sessoes(paciente_id);
CREATE INDEX IF NOT EXISTS idx_sessoes_data ON sessoes(data_sessao);
CREATE INDEX IF NOT EXISTS idx_sessoes_origem ON sessoes(origem);
CREATE INDEX IF NOT EXISTS idx_agendamentos_paciente ON agendamentos(paciente_id);
CREATE INDEX IF NOT EXISTS idx_agendamentos_data ON agendamentos(data);
CREATE INDEX IF NOT EXISTS idx_nf_sessao ON notas_fiscais(sessao_id);

-- Comentários das colunas
COMMENT ON TABLE pacientes IS 'Registros de pacientes da Psicologia Conscience';
COMMENT ON TABLE sessoes IS 'Registros de sessões de atendimento';
COMMENT ON TABLE agendamentos IS 'Agendamentos futuros de sessões';
COMMENT ON TABLE notas_fiscais IS 'Registro de notas fiscais emitidas';

-- ════════════════════════════════════════════════════════════════════════════
-- INSERIR DADOS DE EXEMPLO (opcional)
-- ════════════════════════════════════════════════════════════════════════════

-- Descomente abaixo se quiser inserir dados de exemplo:

/*
INSERT INTO pacientes (nome, email, telefone) VALUES
  ('ANDRE', 'andre@example.com', '71999999999'),
  ('CAROL', 'carol@example.com', '71988888888'),
  ('DANIELA', 'daniela@example.com', '71987654321'),
  ('EDSON', 'edson@example.com', '71986543210');

INSERT INTO sessoes (paciente_id, data_sessao, origem, tipo, valor, status_pagamento, forma_pagamento) VALUES
  (1, '2026-05-15', 'particular', 'individual', 150.00, 'pendente', 'PIX'),
  (2, '2026-04-06', 'particular', 'individual', 100.00, 'pendente', 'Cartão'),
  (3, '2026-05-08', 'particular', 'individual', 150.00, 'pago', 'PIX');
*/
