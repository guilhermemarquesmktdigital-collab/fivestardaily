#!/usr/bin/env python3
"""Encrypt a numbers snapshot for the admin panel.
Usage: python3 _src/admin/make_snapshot.py data.json   (writes admin/snapshot.enc.json)
data.json: {"period": "...", "site": {clicks, impressions, ctr, position, prev{}, top_pages[{page,clicks}], top_queries[{query,clicks,impressions}], note},
            "ig": {handle, followers, following, posts, followers_prev, scheduled[{when,type,title}], recent[{date,type,title,reach,likes}], note}}
Hybrid encryption: random AES-256-GCM key, wrapped with the RSA-OAEP public key stored in admin/vault.json.
Only someone who unlocks the vault (passphrase) can read it."""
import sys, json, os, base64, datetime
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
vault = json.load(open(os.path.join(root, 'admin/vault.json')))
pub = serialization.load_der_public_key(base64.b64decode(vault['pub']))
data = json.load(open(sys.argv[1]))
data['generated_at'] = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
key, iv = os.urandom(32), os.urandom(12)
ct = AESGCM(key).encrypt(iv, json.dumps(data, ensure_ascii=False).encode(), None)
ek = pub.encrypt(key, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
out = {'v': 1, 'ek': base64.b64encode(ek).decode(), 'iv': base64.b64encode(iv).decode(), 'ct': base64.b64encode(ct).decode()}
json.dump(out, open(os.path.join(root, 'admin/snapshot.enc.json'), 'w'))
print('snapshot written', len(ct), 'bytes')
