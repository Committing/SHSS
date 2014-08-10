#v1.0.2

import time

print "Enter .SHSS absolute file path: (Drag and drop it here)"
shssFilePath = raw_input()
#shssFilePath = "/Users/User/Desktop/styles.shss"

print "Enter .css absolute file path: (Drag and drop it here)"
cssFilePath = raw_input()
#cssFilePath = "/Users/User/Desktop/styles.css"

print "SHSS and CSS files loaded."
print "=========================="
print "Scanning..."




def repeater():
	scanFiles()
	time.sleep(3)

def parseSHSS(shssCode):
	conversionArray = [
		['ac', 		'accelerator'],
		['bg', 		'background'],
		['bga', 	'background-attachment'],
		['ba', 		'background-attachment'],
		['bgc', 	'background-color'],
		['bc', 		'background-color'],
		['bgi', 	'background-image'],
		['bi', 		'background-image'],
		['bp', 		'background-position'],
		['bgp', 	'background-position'],
		['bpx', 	'background-position-x'],
		['bx', 		'background-position-x'],
		['bpy',		'background-position-y'],
		['by', 		'background-position-y'],
		['br', 		'background-repeat'],
		['bgr', 	'background-repeat'],
		['bh', 		'behavior'],
		['bo', 		'border'],
		['bb', 		'border-bottom'],
		['bbc', 	'border-bottom-color'],
		['bbs', 	'border-bottom-style'],
		['bbw', 	'border-bottom-width'],
		['boc', 	'border-collapse'],
		['bc', 		'border-color'],
		['bl',		'border-left'],
		['bol',		'border-left'],
		['blc', 	'border-left-color'],
		['bls', 	'border-left-style'],
		['blw', 	'border-left-width'],
		['bor',		'border-right'],
		['brc', 	'border-right-color'],
		['brs',		'border-right-style'],
		['brw',		'border-right-width'],
		['bs', 		'border-style'],
		['bt', 		'border-top'],
		['btc', 	'border-top-color'],
		['bts', 	'border-top-style'],
		['btw', 	'border-top-width'],
		['bw', 		'border-width'],
		['b', 		'bottom'],
		['cs',		'caption-slide'],
		['cl', 		'clear'],
		['cl', 		'clip'],
		['c', 		'color'],
		['con',		'content'],
		['ci', 		'counter-increment'],
		['cr', 		'counter-reset'],
		['cu', 		'cue'],
		['cua',		'cue-after'],
		['cub', 	'cue-before'],
		['cur',		'cursor'],
		['dir', 	'direction'],
		['d', 		'display'],
		['dis', 	'display'],
		['ele',		'elevation'],
		['el',		'elevation'],
		['ec', 		'empty-cells'],
		['em', 		'empty-cells'],
		['fil',		'filter'],
		['fl', 		'float'],
		['f', 		'float'],
		['fo', 		'font'],
		['ff', 		'font-family'],
		['fs', 		'font-size'],
		['fsa',		'font-size-adjust'],
		['fsr',		'font-stretch'],
		['fst', 	'font-style'],
		['fv', 		'font-variant'],
		['fw', 		'font-weight'],
		['h', 		'height'],
		['im', 		'ime-mode'],
		['is', 		'include-source'],
		['lbc',		'layer-background-color'],
		['lbi',		'layer-background-image'],
		['lf', 		'layer-flow'],
		['lg', 		'layout-grid'],
		['lgc',		'layout-grid-char'],
		['lgcs', 	'layout-grid-char-spacing'],
		['lgl',		'layout-grid-line'],
		['lgm',		'layout-grid-mode'],
		['lgt',		'layout-grid-type'],
		['l', 		'left'],
		['ls', 		'letter-spacing'],
		['lb', 		'line-break'],
		['lh', 		'line-height'],
		['ls', 		'list-style'],
		['lsi',		'list-style-image'],
		['lsp', 	'list-style-position'],
		['lst',		'list-style-type'],
		['m', 		'margin'],
		['mb', 		'margin-bottom'],
		['ml', 		'margin-left'],
		['mr', 		'margin-right'],
		['mt', 		'margin-top'],
		['mo', 		'marker-offset'],
		['ma', 		'marks'],
		['mh', 		'max-height'],
		['mw', 		'max-width'],
		['mih', 	'min-height'],
		['miw',		'min-width'],
		['or', 		'orphans'],
		['ou', 		'outline'],
		['ouc',		'outline-color'],
		['ous',		'outline-style'],
		['ouw',		'outline-width'],
		['oc',		'outline-color'],
		['os',		'outline-style'],
		['ow',		'outline-width'],
		['o', 		'overflow'],
		['ox', 		'overflow-x'],
		['oy', 		'overflow-y'],
		['p', 		'padding'],
		['pb', 		'padding-bottom'],
		['pl', 		'padding-left'],
		['pr', 		'padding-right'],
		['pt', 		'padding-top'],
		['pa', 		'page'],
		['pba', 	'page-break-after'],
		['pbb',		'page-break-before'],
		['pbi', 	'page-break-inside'],
		['pau',		'pause'],
		['pa', 		'pause-after'],
		['pb', 		'pause-before'],
		['pi', 		'pitch'],
		['pr', 		'pitch-range'],
		['pd', 		'play-duration'],
		['pos', 	'position'],
		['po', 		'position'],
		['q', 		'quotes'],
		['ri', 		'richness'],
		['r', 		'right'],
		['ra', 		'ruby-align'],
		['ro', 		'ruby-overhang'],
		['rp', 		'ruby-position'],
		['s', 		'size'],
		['sp', 		'speak'],
		['sh', 		'speak-header'],
		['sn', 		'speak-numeral'],
		['sp', 		'speak-punctuation'],
		['sr', 		'speach-rate'],
		['st', 		'stress'],
		['sac', 	'scrollbar-arrow-color'],
		['sbc', 	'scroll-base-color'],
		['sdsc',	'scrollbar-dark-shadow-color'],
		['sfc',		'scrollbar-face-color'],
		['shc',		'scrollbar-highlight-color'],
		['ssc', 	'scrollbar-shadow-color'],
		['s3l',		'scrollbar-3d-light'],
		['stc',		'scrollar-track-color'],
		['tl', 		'table-layout'],
		['ta', 		'text-align'],
		['tal',		'text-align-last'],
		['td', 		'text-decoration'],
		['ti', 		'text-indent'],
		['tj', 		'text-justify'],
		['to', 		'text-overflow'],
		['ts', 		'text-shadow'],
		['tt', 		'text-transform'],
		['ta', 		'text-autospace'],
		['tks',		'text-kashida-space'],
		['tup',		'text-underline-position'],
		['t', 		'top'],
		['ub', 		'unicode-bidi'],
		['va', 		'vertical-align'],
		['v', 		'visibility'],
		['vf', 		'voice-family'],
		['vo', 		'volume'],
		['ws', 		'white-space'],
		['wid',		'widows'],
		['w', 		'width'],
		['wb', 		'word-break'],
		['ws', 		'word-spacing'],
		['ww', 		'word-wrap'],
		['wm', 		'writhing-mode'],
		['z', 		'z-index'],
		['zi', 		'z-index'],
		['zo', 		'zoom']
	]
	for shortSHSS, longCSS in conversionArray:
		#Different conversions for different situations:
		shssCode = shssCode.replace('\t' + shortSHSS + ':', '\t' + longCSS + ':')
		shssCode = shssCode.replace('\n' + shortSHSS + ':', '\n' + longCSS + ':')
		shssCode = shssCode.replace(' ' + shortSHSS + ':', ' ' + longCSS + ':')
		shssCode = shssCode.replace(';' + shortSHSS + ':', ';' + longCSS + ':')
		shssCode = shssCode.replace('; ' + shortSHSS + ':', '; ' + longCSS + ':')
	return shssCode

def scanFiles():
	shssFileContents = open(shssFilePath, 'r').read()
	cssFileContents  = open(cssFilePath, 'r').read()
	shssFileContents = parseSHSS(shssFileContents)
	if shssFileContents == cssFileContents:
		print "Files identical"
	else:
		cssFile  = open(cssFilePath, 'w').write(shssFileContents)
		print "CSS file updated"





#Start the scan
while True:
	repeater()
