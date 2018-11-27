dna_strand_1 = &quot;ITRG-CGG-GAC-CIG-GCC-GTC&quot; # TAG-GCC-CTG-GTC-GAC-
CGG-CAG
dna_strand_2 = &quot;&quot;
for x in range(len(dna_strand_1)):
char = dna_strand_1[x]
if char == &quot;A&quot;:
dna_strand_2 += &quot;B&quot;
elif char == &quot;B&quot;:
dna_strand_2 += &quot;C&quot;
elif char == &quot;C&quot;:
dna_strand_2 += &quot;D&quot;
elif char == &quot;D&quot;:
dna_strand_2 += &quot;E&quot;
elif char == &quot;E&quot;:
dna_strand_2 += &quot;F&quot;
elif char == &quot;F&quot;:
dna_strand_2 += &quot;G&quot;
elif char == &quot;G&quot;:
dna_strand_2 += &quot;H&quot;
elif char == &quot;H&quot;:
dna_strand_2 += &quot;I&quot;
elif char == &quot;I&quot;:
dna_strand_2 += &quot;J&quot;
elif char == &quot;J&quot;:
dna_strand_2 += &quot;K&quot;
elif char == &quot;K&quot;:
dna_strand_2 += &quot;L&quot;
elif char == &quot;L&quot;:
dna_strand_2 += &quot;M&quot;
elif char == &quot;M&quot;:
dna_strand_2 += &quot;N&quot;
elif char == &quot;N&quot;:

dna_strand_2 += &quot;O&quot;
elif char == &quot;O&quot;:
dna_strand_2 += &quot;P&quot;
elif char == &quot;P&quot;:
dna_strand_2 += &quot;Q&quot;
elif char == &quot;Q&quot;:
dna_strand_2 += &quot;R&quot;
elif char == &quot;R&quot;:
dna_strand_2 += &quot;S&quot;
elif char == &quot;S&quot;:
dna_strand_2 += &quot;T&quot;
elif char == &quot;T&quot;:
dna_strand_2 += &quot;U&quot;
elif char == &quot;U&quot;:
dna_strand_2 += &quot;V&quot;
elif char == &quot;V&quot;:
dna_strand_2 += &quot;W&quot;
elif char == &quot;W&quot;:
dna_strand_2 += &quot;X&quot;
elif char == &quot;X&quot;:
dna_strand_2 += &quot;Y&quot;
elif char == &quot;Y&quot;:
dna_strand_2 += &quot;Z&quot;
elif char == &quot;Z&quot;:
dna_strand_2 += &quot;A&quot;
else:
dna_strand_2 += char
print(dna_strand_2)
