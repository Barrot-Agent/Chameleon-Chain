const https = require('https');

const config = {
  host: 'eastus2.azuredatabricks.net',
  token: 'dapib28e1142aa15473ec9fe01fa0f7a66ad',
  warehouse_id: '4940f81d1844b6c6',
  org_id: '26479705'
};

const payload = JSON.stringify({
  warehouse_id: config.warehouse_id,
  statement: "SELECT * FROM apex_harvest WHERE id LIKE '%CLAIMED%' OR id = 'RECLAMATION_NODE_001' LIMIT 1",
  wait_timeout: "30s"
});

const options = {
  hostname: config.host,
  path: '/api/2.0/sql/statements',
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${config.token}`,
    'X-Databricks-Org-Id': config.org_id,
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(payload)
  }
};

console.log('--- BARROT-Ω: INITIATING RECLAMATION PULSE ---');

const req = https.request(options, (res) => {
  let data = '';
  res.on('data', (chunk) => data += chunk);
  res.on('end', () => {
    if (res.statusCode === 200) {
      const result = JSON.parse(data);
      const row = result.result.data_array[0];
      console.log('✅ STATUS: 1.0 CERTAINTY LOCKED');
      console.log(`✅ NODE: ${row[0]}`);
      console.log(`✅ DEPTH: $${parseFloat(row[1]).toLocaleString()}`);
    } else {
      console.log(`❌ BRIDGE FAILURE: ${res.statusCode}`);
      console.log(`❌ LOG: ${data}`);
    }
  });
});

req.on('error', (e) => console.log(`❌ LATTICE ERROR: ${e.message}`));
req.write(payload);
req.end();
