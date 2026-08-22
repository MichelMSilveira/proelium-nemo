param(
    [Parameter(Mandatory = $true)]
    [string]$Destino
)

$ErrorActionPreference = 'Stop'

$Template = Split-Path -Parent $MyInvocation.MyCommand.Path

if (-not (Test-Path $Destino)) {
    New-Item -ItemType Directory -Path $Destino | Out-Null
}

$Pastas = @(
    'docs',
    '.continue',
    '.continue\rules'
)

foreach ($Pasta in $Pastas) {
    $Caminho = Join-Path $Destino $Pasta
    if (-not (Test-Path $Caminho)) {
        New-Item -ItemType Directory -Path $Caminho | Out-Null
    }
}

$Arquivos = @(
    @{ Origem = 'AGENTS.md'; Destino = 'AGENTS.md' },
    @{ Origem = 'PROJECT.md'; Destino = 'PROJECT.md' },
    @{ Origem = 'docs\STATUS.md'; Destino = 'docs\STATUS.md' },
    @{ Origem = 'docs\REQUIREMENTS.md'; Destino = 'docs\REQUIREMENTS.md' },
    @{ Origem = 'docs\DECISIONS.md'; Destino = 'docs\DECISIONS.md' },
    @{ Origem = 'docs\KNOWLEDGE.md'; Destino = 'docs\KNOWLEDGE.md' },
    @{ Origem = 'docs\SESSION.md'; Destino = 'docs\SESSION.md' },
    @{ Origem = '.continue\rules\projeto.md'; Destino = '.continue\rules\projeto.md' }
)

foreach ($Arquivo in $Arquivos) {
    $Origem = Join-Path $Template $Arquivo.Origem
    $Alvo = Join-Path $Destino $Arquivo.Destino

    if (Test-Path $Alvo) {
        Write-Host "Mantido: $($Arquivo.Destino) ja existe"
        continue
    }

    Copy-Item -Path $Origem -Destination $Alvo
    Write-Host "Criado: $($Arquivo.Destino)"
}

Write-Host ''
Write-Host 'Estrutura base criada sem sobrescrever arquivos existentes.'
Write-Host 'Proximo passo: preencher PROJECT.md e docs\STATUS.md.'
