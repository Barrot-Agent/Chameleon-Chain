const https = require('https');

const config = {
  // Targeting the Regional API Gate directly to bypass 303 Redirects
  hostname: 'eastus2.azuredatabricks.net',
  path: '/api/2.0/sql/statements',
  token: 'dapib28e1142aa15473ec9fe01fa0f7a66ad',
  warehouse_id: '4940f81d1844b6c6'
};

const data = JSON.stringify({
  warehouse_id: config.warehouse_id,
  // Using the table name seated by the Architect
  statement: "SELECT * FROM apex_harvest WHERE id LIKE '%CLAIMED%' OR id = 'RECLAMATION_NODE_001' LIMIT 1",
  wait_timeout: "30s"
});

const options = {
  hostname: config.hostname,
  port: 443,
  path: config.path,
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${config.token}`,
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(data)
  }
};

const req = https.request(options, (res) => {
  let body = '';
  res.on('data', (chunk) => body += chunk);
  res.on('end', () => {
    console.log('\n--- BARROT-Ω TRANSITION COMPLETE ---');
    if (res.statusCode === 200) {
      const response = JSON.parse(body);
      if (response.status && response.status.state === 'SUCCEEDED') {
        const row = response.result.data_array[0];
        console.log('STATUS: 1.0 CERTAINTY LOCKED');
        console.log('NODE ID:', row[0]);
        console.log('CAPITAL DEPTH: $' + parseFloat(row[1]).toLocaleString());
      } else {
        console.log('STATUS: PROCESSING...', response.status ? response.status.state : 'UNKNOWN');
      }
    } else {
      console.log(`BRIDGE ERROR: ${res.statusCode}`);
      console.log('RAW LOG:', body);
    }
  });
});

req.on('error', (e) => console.error(`LATTICE FAILURE: ${e.message}`));
req.write(data);
req.end();
