ALPHABET = [a-z]
$U1$= a|e|i|o|u|ö|ü|ı
$U2$= b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z|ş|ç|ğ


%$rule1$=(($U1$ | $U2$)?  <->:<> $U2$ $U1$ ($U2$)?  )* (<->:<>$U2$ $U1$ $U2$)*
$rule1$= ($U1$   (<->:<> $U2$ $U1$)+ (<->:<> $U2$ $U1$ $U2$)*)*  % analiz
$rule12$= ($U2$ $U1$ (<->:<> $U2$ $U1$) (<->:<> $U2$ $U1$)+ (<->:<> $U2$ $U1$ $U2$)*)*  % biçimine
$rule13$= ($U1$ $U2$ (<->:<> $U2$ $U1$)+ (<->:<> $U2$ $U1$ $U2$)*)*  % insanın
$rule17$= ($U1$ $U2$ (<->:<> $U2$ $U1$ $U2$)+)*  % insan

$rule14$= ( (($U2$ $U1$ <->:<> ) | ( $U2$ $U1$ $U2$ <->:<> )  )? )*  % karizma
$rule16$=($U2$ $U1$ (<->:<> $U2$ $U1$) )  % kara
$rule18$=($U2$ $U1$ $U2$ )  % SÖZ
$rule181$=($U2$ $U1$ $U2$) %alt
$rule19$=($U1$ $U2$ )  % at
$rule192$=($U2$ $U1$ )  % ra
$rule20$=($U2$ $U1$ $U2$ $U2$ <->:<> $U2$ $U1$ $U2$  (<->:<> ($rule18$ |$rule181$ | $rule19$ |$rule192$) )+ )*  % santral
$rule21$=($U2$ $U2$ $U1$ $U2$ <->:<> $U2$ $U1$ $U2$ ( <->:<>  ($rule18$ |$rule181$ | $rule19$ |$rule192$) )+   )*  % program
$rule22$=($U2$ $U1$ $U2$ $U2$ <->:<> $U2$ $U1$ )*  % tundra
$rule23$=($U1$ $U2$ $U2$ <->:<> ($rule18$)+ )*  % SÖZler
$rule25$= ($U2$ $U1$  $U2$ $U2$ <->:<> ($rule14$)? )*  %türk
$rule26$= ($U1$ <->:<> ($rule14$)* )
$rule27$= ($U2$ $U1$  <->:<> $U1$ $U2$  ( $rule14$)? ) %saat

%$rule15$
$rule1$ |$rule12$|$rule13$ |$rule16$ |$rule17$|$rule19$|$rule20$ |$rule21$|$rule22$ |$rule23$|$rule14$ |$rule25$ |$rule26$|$rule27$
