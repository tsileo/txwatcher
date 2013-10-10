===========
 TxWatcher
===========

A little Python utility that lets you monitor Bitcoin addresses through `Blockchain Websocket API <http://blockchain.info/api/api_websocket>`_ and perform custom callbacks.


.. image:: https://pypip.in/v/txwatcher/badge.png
        :target: https://crate.io/packages/txwatcher

.. image:: https://pypip.in/d/txwatcher/badge.png
        :target: https://crate.io/packages/txwatcher


Installation
============

.. code-block::

    $ pip install txwatcher


QuickStart
==========

.. code-block:: python

	from txwatcher import TxWatcher

	w = TxWatcher(['18eGUUxUsSetQYxJcQXEQTjSCUETEFeA4E'])

	def tx_printer(tx):
		print(tx)

	# You can add as many callbacks as you want
	w.on_tx += tx_printer

	w.run_forever()
	# or
	import thread
	thread.start_new_thread(w.run_forever, ())
	
	# Do some work

	w.add_addresses(*['16xg9kBKUR2S6bmyccCyPichCpMNMPATAH'])


Transactions format
-------------------

.. code-block:: python

	{
	    "op": "utx",
	    "x": {
	        "hash": "f6c51463ea867ce58588fec2a77e9056046657b984fd28b1482912cdadd16374",
	        "ver": 1,
	        "vin_sz": 4,
	        "vout_sz": 2,
	        "lock_time": "Unavailable",
	        "size": 796,
	        "relayed_by": "209.15.238.250",
	        "tx_index": 3187820,
	        "time": 1331300839,
	        "inputs": [
	            {
	                "prev_out": {
	                    "value": 10000000,
	                    "type": 0,
	                    "addr": "12JSirdrJnQ8QWUaGZGiBPBYD19LxSPXho"
	                }
	            }
	        ],
	        "out": [
	            {
	                "value": 2800000000,
	                "type": 0,
	                "addr": "1FzzMfNt46cBeS41r6WHDH1iqxSyzmxChw"
	            }
	        ]
	    }
	}


Misc
----

Using TxWatcher within Flask
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can start TxWatcher in a separate thread and have it running within your Flask app (or any Python web framework).

.. code-block:: python

	from flask import Flask
	app = Flask(__name__)

	@app.route("/")
	def hello():
	    return "Hello World!"

	if __name__ == "__main__":
	    # First, start TxWatcher
	    tw = TxWatcher([a['address'] for a in col_urls.find()])
	    tw.on_tx += new_tx

	    thread.start_new_thread(tw.run_forever, ())

	    # Then, start the Flask app
	    app.run()


Contribution
============

Feel free to submit a pull request!


Donation
========

If you like my work, please consider donating:

BTC 18eGUUxUsSetQYxJcQXEQTjSCUETEFeA4E


License (MIT)
=============

Copyright (c) 2013 Thomas Sileo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
