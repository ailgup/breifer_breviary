class MagnificatTextStyle(PropertySet):
 defaults = {
 'fontName':'Arno',
 'fontSize':10,
 'leading':12,
 'leftIndent':0,
 'rightIndent':0,
 'firstLineIndent':0,
 'alignment':TA_LEFT,
 'spaceBefore':0,
 'spaceAfter':0,
 'bulletFontName':_baseFontName,
 'bulletFontSize':10,
 'bulletIndent':0,
 'textColor': black,
 'backColor':None,
 'wordWrap':None,
 'borderWidth': 0,
 'borderPadding': 0,
 'borderColor': None,
 'borderRadius': None,
 'allowWidows': 1,
 'allowOrphans': 0,
 'textTransform':None,
 'endDots':None,
 'splitLongWords':1,
 'underlineWidth': _baseUnderlineWidth,
 'bulletAnchor': 'start',
 'justifyLastLine': 0,
 'justifyBreaks': 0,
 'spaceShrinkage': _spaceShrinkage,
 'strikeWidth': _baseStrikeWidth, #stroke width
 'underlineOffset': _baseUnderlineOffset, #fraction of fontsize to offset underlines
 'underlineGap': _baseUnderlineGap, #gap for double/triple underline
 'strikeOffset': _baseStrikeOffset, #fraction of fontsize to offset strikethrough
 'strikeGap': _baseStrikeGap, #gap for double/triple strike
 'linkUnderline': _platypus_link_underline,
 #'underlineColor': None,
 #'strikeColor': None,
 'hyphenationLang': _hyphenationLang,
 'uriWasteReduce': _uriWasteReduce,
 'embeddedHyphenation': _embeddedHyphenation,
 }