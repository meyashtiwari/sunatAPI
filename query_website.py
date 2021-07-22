from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
PATH = ".\\msedgedriver.exe"

def get_result(data):
    driver = webdriver.Edge(PATH)
    driver.get("https://ww1.sunat.gob.pe/ol-ti-itconsvalicpe/ConsValiCpe.htm")

    ruc_number_field = driver.find_element_by_name("num_ruc")
    ruc_number_field.send_keys(data['ruc_number'])

    voucher_type_options = driver.find_element_by_name("tipocomprobante")
    voucher_type_select = Select(voucher_type_options)
    voucher_type_select.select_by_value(data['voucher_type'])

    document_type_options = driver.find_element_by_name("cod_docide")
    document_type_select = Select(document_type_options)
    document_type_select.select_by_value(data['document_type'])

    if(data['document_type'] != '-'):
        document_number_field = driver.find_element_by_name("num_docide")
        document_number_field.send_keys(data['document_number'])

    voucher_serial_field = driver.find_element_by_name("num_serie")
    voucher_serial_field.send_keys(data['voucher_serial'])
    voucher_number_field = driver.find_element_by_name("num_comprob")
    voucher_number_field.send_keys(data['voucher_number'])

    date_of_issue_field = driver.find_element_by_name("fec_emision")
    date_of_issue_field.send_keys(data['date_of_issue'])

    total_fees_field = driver.find_element_by_name("cantidad")
    total_fees_field.send_keys(data['total_amount'])

    submit_button = driver.find_element_by_name("wacepta")
    driver.execute_script("arguments[0].click();", submit_button)

    result_message = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td.bgn"))).get_attribute("innerHTML")

    return {'result': result_message}