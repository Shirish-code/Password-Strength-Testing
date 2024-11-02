
### 3. `usage.md`
Guide on how to use Hashcat with the files provided.

```markdown
# Usage Guide

## Running Hashcat
1. Open a terminal and navigate to the `hashcat-6.2.6` folder.
2. Run Hashcat with the following command:
   ```bash
   ./hashcat.bin -m 0 -a 0 ../hashes.txt ../passwords.txt --force --status

Parameters
-m 0: Specifies MD5 hash type.
-a 0: Straight attack mode.
../hashes.txt: File containing hashes.
../passwords.txt: File containing passwords.
