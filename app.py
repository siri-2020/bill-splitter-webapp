"""
Bill Splitter Web Application
A Flask-based web app for splitting restaurant bills fairly among multiple people.
"""

from flask import Flask, render_template, request, jsonify, send_file
import os
from datetime import datetime
import io

app = Flask(__name__)

# Data storage (in-memory for simplicity)
bills = {}

@app.route('/')
def index():
    """Render the main application page."""
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate_bill():
    """Calculate bill split based on dishes and assignments."""
    try:
        data = request.json
        dishes = data.get('dishes', [])
        people = data.get('people', [])
        assignments = data.get('assignments', {})
        
        # Initialize totals
        person_totals = {person: 0.0 for person in people}
        
        # Calculate shared costs
        for dish in dishes:
            dish_name = dish['name']
            dish_price = float(dish['price'])
            eaters = assignments.get(dish_name, [])
            
            if len(eaters) > 0:
                price_per_person = dish_price / len(eaters)
                for eater in eaters:
                    if eater in person_totals:
                        person_totals[eater] += price_per_person
        
        # Calculate total bill
        total_bill = sum(float(dish['price']) for dish in dishes)
        
        # Create result
        results = [
            {'name': person, 'amount': round(total, 2)}
            for person, total in person_totals.items()
        ]
        
        # Store bill for later retrieval
        bill_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        bills[bill_id] = {
            'results': results,
            'total': round(total_bill, 2),
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify({
            'success': True,
            'results': results,
            'total': round(total_bill, 2),
            'bill_id': bill_id
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/download/<bill_id>')
def download_bill(bill_id):
    """Download bill summary as text file."""
    try:
        if bill_id not in bills:
            return "Bill not found", 404
        
        bill = bills[bill_id]
        
        # Create text content
        content = "===== Bill Summary =====\n"
        content += f"Created: {bill['timestamp']}\n\n"
        
        for result in bill['results']:
            content += f"{result['name']}: THB {result['amount']:.2f}\n"
        
        content += f"\nTotal Bill: THB {bill['total']:.2f}\n"
        content += "=========================\n"
        
        # Create file-like object
        file_obj = io.BytesIO(content.encode('utf-8'))
        file_obj.seek(0)
        
        return send_file(
            file_obj,
            mimetype='text/plain',
            as_attachment=True,
            download_name=f'bill_{bill_id}.txt'
        )
    
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
