from flask import Blueprint, request, redirect, url_for
from flask import render_template, flash

from dataissues.util import jsonify

api = Blueprint('api', __name__)


@api.route('/', methods=['GET'])
def root():
    return jsonify({"status": "Banana!"})
