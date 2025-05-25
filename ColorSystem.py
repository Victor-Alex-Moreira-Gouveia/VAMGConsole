class FontColorError(Exception):
    """Base exception for FontColor class errors."""
    pass

class InvalidFontTypeError(FontColorError):
    """Exception raised when an invalid font type is provided."""
    def __init__(self, font_type, available_options):
        self.font_type = font_type
        self.available_options = available_options
        self.message = f"Opção de fonte indisponível: '{font_type}'. Opções disponíveis: {available_options}"
        super().__init__(self.message)

class InvalidColorError(FontColorError):
    """Exception raised when an invalid color is provided."""
    def __init__(self, color, available_options):
        self.color = color
        self.available_options = available_options
        self.message = f"Opção de cor indisponível: '{color}'. Opções disponíveis: {available_options}"
        super().__init__(self.message)

class FontColor:
    # Opções disponíveis
    FONT_TYPES = ['normal', 'bold', 'underline', 'italic', 'strikethrough', 'blink', 'hidden', 'reverse', 'dim']
    COLORS = ['red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white']
    
    # Constante para reset completo
    RESET_ALL = '\033[0m'
    
    # Códigos ANSI para formatação
    FONT_CODES = {
        'normal': '',  # Normal não aplica formatação especial
        'bold': '\033[1m',
        'underline': '\033[4m',
        'italic': '\033[3m',
        'strikethrough': '\033[9m',
        'blink': '\033[5m',
        'hidden': '\033[8m',
        'reverse': '\033[7m',
        'dim': '\033[2m'
    }
    
    # Códigos ANSI para cores
    COLOR_CODES = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m'
    }
    
    def __init__(self, text, type_font, color_font):
        """
        Inicializa um objeto FontColor com texto formatado.
        
        Args:
            text: O texto a ser formatado
            type_font: O tipo de fonte ('normal', 'bold', 'underline', 'italic', 'strikethrough', 'blink', 'hidden', 'reverse', 'dim')
            color_font: A cor do texto ('red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white')
            
        Raises:
            InvalidFontTypeError: Se o tipo de fonte não for válido
            InvalidColorError: Se a cor não for válida
            TypeError: Se houver erro na conversão de tipos
        """
        try:
            self.text = str(text)
            self.type_font = str(type_font).lower()
            self.color_font = str(color_font).lower()
            
            # Validação centralizada
            self._validate_input()
            
            # Formata o texto com a fonte e cor especificadas
            self.formatted_text = self._format_text()
            
        except TypeError as e:
            raise TypeError(f"Erro de tipo ao processar os parâmetros: {e}")
    
    def _validate_input(self):
        """Valida os tipos de fonte e cores fornecidos."""
        # Validar tipo de fonte
        if self.type_font not in self.FONT_TYPES:
            raise InvalidFontTypeError(self.type_font, self.FONT_TYPES)
        
        # Validar cor
        if self.color_font not in self.COLORS:
            raise InvalidColorError(self.color_font, self.COLORS)
    
    def _format_text(self):
        """
        Formata o texto com a fonte e cor escolhidas.
        
        Importante: O código ANSI não fornece um modo para resetar apenas a formatação
        mantendo a cor. Por isso, estamos armazenando o texto formatado sem o código
        de reset. O reset será aplicado apenas quando o texto for convertido para string
        pelo método __str__().
        """
        # Obtém os códigos ANSI para a cor e a fonte
        color_code = self.COLOR_CODES[self.color_font]
        font_code = self.FONT_CODES[self.type_font]
        
        # Não aplicamos o reset aqui para evitar perder a formatação
        # O reset será aplicado apenas no método __str__
        
        # Para 'normal', não precisamos aplicar nenhum código de formatação adicional
        if self.type_font == 'normal':
            return f"{color_code}{self.text}"
        else:
            return f"{color_code}{font_code}{self.text}"
    
    def __str__(self):
        """
        Retorna o texto formatado quando o objeto é convertido para string.
        Aplica o reset apenas no final para garantir que a formatação não
        afete textos subsequentes.
        """
        return f"{self.formatted_text}{self.RESET_ALL}"


# Exemplos de uso:
# Variavel = FontColor("text", type_font, color_font)

"""Lógica do sitema de cor de fundo

Backgroud = BC(variavel, Cor_fundo)
""" 