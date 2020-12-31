import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MiniDecafParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, Int=2, Return=3, If=4, Else=5, For=6, Do=7, While=8, Break=9, 
		Continue=10, Lparen=11, Rparen=12, Lbrkt=13, Rbrkt=14, Lbrace=15, Rbrace=16, 
		Comma=17, Semicolon=18, Punctuator=19, Plus=20, Minus=21, Asterisk=22, 
		Slash=23, Percent=24, Exclamation=25, Tilde=26, Ampersand=27, Langle=28, 
		Rangle=29, Langle_eq=30, Rangle_eq=31, Double_eq=32, Exclam_eq=33, Equal=34, 
		Double_amp=35, Double_bar=36, Operator=37, Integer=38, Whitespace=39, 
		Ident=40;
	public static final int
		RULE_function = 0, RULE_returntype = 1, RULE_main = 2, RULE_content = 3;
	public static final String[] ruleNames = {
		"function", "returntype", "main", "content"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'main'", "'int'", "'return'", "'if'", "'else'", "'for'", "'do'", 
		"'while'", "'break'", "'continue'", "'('", "')'", "'['", "']'", "'{'", 
		"'}'", "','", "';'", null, "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'~'", 
		"'&'", "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'='", "'&&'", "'||'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, "Int", "Return", "If", "Else", "For", "Do", "While", "Break", 
		"Continue", "Lparen", "Rparen", "Lbrkt", "Rbrkt", "Lbrace", "Rbrace", 
		"Comma", "Semicolon", "Punctuator", "Plus", "Minus", "Asterisk", "Slash", 
		"Percent", "Exclamation", "Tilde", "Ampersand", "Langle", "Rangle", "Langle_eq", 
		"Rangle_eq", "Double_eq", "Exclam_eq", "Equal", "Double_amp", "Double_bar", 
		"Operator", "Integer", "Whitespace", "Ident"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "MiniDecaf.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MiniDecafParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class FunctionContext extends ParserRuleContext {
		public ReturntypeContext returntype() {
			return getRuleContext(ReturntypeContext.class,0);
		}
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_function);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(8);
			returntype();
			setState(9);
			main();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReturntypeContext extends ParserRuleContext {
		public ReturntypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returntype; }
	}

	public final ReturntypeContext returntype() throws RecognitionException {
		ReturntypeContext _localctx = new ReturntypeContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_returntype);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(11);
			match(Int);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MainContext extends ParserRuleContext {
		public TerminalNode Lparen() { return getToken(MiniDecafParser.Lparen, 0); }
		public TerminalNode Rparen() { return getToken(MiniDecafParser.Rparen, 0); }
		public TerminalNode Lbrace() { return getToken(MiniDecafParser.Lbrace, 0); }
		public ContentContext content() {
			return getRuleContext(ContentContext.class,0);
		}
		public TerminalNode Rbrace() { return getToken(MiniDecafParser.Rbrace, 0); }
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_main);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13);
			match(T__0);
			setState(14);
			match(Lparen);
			setState(15);
			match(Rparen);
			setState(16);
			match(Lbrace);
			setState(17);
			content();
			setState(18);
			match(Rbrace);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ContentContext extends ParserRuleContext {
		public TerminalNode Integer() { return getToken(MiniDecafParser.Integer, 0); }
		public ContentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_content; }
	}

	public final ContentContext content() throws RecognitionException {
		ContentContext _localctx = new ContentContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_content);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(20);
			match(Return);
			setState(21);
			match(Integer);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3*\32\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5"+
		"\3\5\3\5\3\5\2\2\6\2\4\6\b\2\2\2\25\2\n\3\2\2\2\4\r\3\2\2\2\6\17\3\2\2"+
		"\2\b\26\3\2\2\2\n\13\5\4\3\2\13\f\5\6\4\2\f\3\3\2\2\2\r\16\7\4\2\2\16"+
		"\5\3\2\2\2\17\20\7\3\2\2\20\21\7\r\2\2\21\22\7\16\2\2\22\23\7\21\2\2\23"+
		"\24\5\b\5\2\24\25\7\22\2\2\25\7\3\2\2\2\26\27\7\5\2\2\27\30\7(\2\2\30"+
		"\t\3\2\2\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}